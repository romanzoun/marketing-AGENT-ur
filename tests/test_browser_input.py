from __future__ import annotations

import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from playwright.async_api import TimeoutError as PlaywrightTimeoutError

from linkedin_agents.browser.linkedin import LinkedInClient


class BrowserInputTests(unittest.IsolatedAsyncioTestCase):
    async def test_write_pause_uses_configured_delay(self) -> None:
        client = LinkedInClient("http://localhost:9222")
        page = MagicMock()
        page.wait_for_timeout = AsyncMock()
        client._page = page
        client._action_delay_ms = 2000

        await client._wait_before_write()

        page.wait_for_timeout.assert_awaited_once_with(2000)

    def test_action_delay_method_returns_configured_value(self) -> None:
        client = LinkedInClient("http://localhost:9222")

        self.assertEqual(client.action_delay_ms(2000), 2000)

    async def test_login_check_tolerates_feed_navigation_timeout_after_commit(self) -> None:
        client = LinkedInClient("http://localhost:9222")
        page = MagicMock()
        page.url = "https://www.linkedin.com/feed/"
        page.goto = AsyncMock(
            side_effect=PlaywrightTimeoutError(
                "Page.goto: Timeout 30000ms exceeded while waiting for domcontentloaded"
            )
        )
        client._page = page

        self.assertTrue(await client.ensure_logged_in())
        page.goto.assert_awaited_once_with(
            "https://www.linkedin.com/feed/", wait_until="domcontentloaded"
        )

    async def test_cdp_connection_uses_playwright_default_timeout(self) -> None:
        page = MagicMock()
        page.url = "https://www.linkedin.com/feed/"
        page.is_closed.return_value = False
        page.evaluate = AsyncMock()
        context = MagicMock()
        context.pages = [page]
        context.grant_permissions = AsyncMock()
        browser = MagicMock()
        browser.contexts = [context]
        playwright = MagicMock()
        playwright.chromium.connect_over_cdp = AsyncMock(return_value=browser)
        playwright.stop = AsyncMock()
        starter = MagicMock()
        starter.start = AsyncMock(return_value=playwright)
        client = LinkedInClient("http://localhost:9222")

        with (
            patch(
                "linkedin_agents.browser.linkedin.async_playwright",
                return_value=starter,
            ),
            patch.object(
                client, "_pick_automation_page", AsyncMock(return_value=page)
            ),
        ):
            async with client as entered:
                self.assertIs(entered.page, page)

        playwright.chromium.connect_over_cdp.assert_awaited_once_with(
            "http://localhost:9222"
        )
        playwright.stop.assert_awaited_once()

    async def test_comment_by_url_stops_when_post_was_removed(self) -> None:
        client = LinkedInClient("http://localhost:9222")
        page = MagicMock()
        page.goto = AsyncMock()
        page.wait_for_timeout = AsyncMock()
        unavailable = MagicMock()
        unavailable.count = AsyncMock(return_value=1)
        page.get_by_text.return_value = unavailable
        client._page = page

        posted = await client.comment_by_url(
            "https://lnkd.in/p/removed", "Dieser Text darf nicht eingegeben werden."
        )

        self.assertFalse(posted)
        page.get_by_role.assert_not_called()
        page.locator.assert_not_called()

    async def test_comment_by_url_uses_accessible_tiptap_editor(self) -> None:
        client = LinkedInClient("http://localhost:9222")
        page = MagicMock()
        page.goto = AsyncMock()
        page.wait_for_timeout = AsyncMock()
        page.evaluate = AsyncMock(return_value="Ein markanter Kommentartext")

        unavailable = MagicMock()
        unavailable.count = AsyncMock(return_value=0)
        page.get_by_text.return_value = unavailable

        comment_button = MagicMock()
        comment_button.count = AsyncMock(return_value=1)
        comment_button.click = AsyncMock()
        comment_button.first = comment_button

        editor = MagicMock()
        editor.wait_for = AsyncMock()
        editor.last = editor

        submit = MagicMock()
        submit.click = AsyncMock()
        submit.last = submit
        page.get_by_role.side_effect = [comment_button, editor, submit]

        client._page = page
        client._set_editor_text = AsyncMock()

        posted = await client.comment_by_url(
            "https://lnkd.in/p/example", "Ein markanter Kommentartext"
        )

        self.assertTrue(posted)
        role = page.get_by_role.call_args_list[1].args[0]
        name = page.get_by_role.call_args_list[1].kwargs["name"]
        self.assertEqual(role, "textbox")
        self.assertIsNotNone(name.search("Text editor for creating comment"))
        self.assertIsNotNone(name.search("Texteditor zum Erstellen eines Kommentars"))
        client._set_editor_text.assert_awaited_once_with(
            editor, "Ein markanter Kommentartext"
        )
        editor.wait_for.assert_awaited_once_with(state="visible", timeout=8000)
        page.locator.assert_not_called()

    async def test_editor_text_is_filled_in_one_operation(self) -> None:
        client = LinkedInClient("http://localhost:9222")
        client._page = MagicMock()
        editor = MagicMock()
        editor.click = AsyncMock()
        editor.fill = AsyncMock()

        await client._set_editor_text(editor, "Zeile eins\nZeile zwei 🚀")

        editor.click.assert_awaited_once()
        editor.fill.assert_awaited_once_with("Zeile eins\nZeile zwei 🚀", timeout=8000)
        client.page.keyboard.insert_text.assert_not_called()

    async def test_editor_uses_cdp_insert_text_as_fallback(self) -> None:
        client = LinkedInClient("http://localhost:9222")
        page = MagicMock()
        page.keyboard.insert_text = AsyncMock()
        client._page = page
        editor = MagicMock()
        editor.click = AsyncMock()
        editor.fill = AsyncMock(side_effect=RuntimeError("Quill blockiert fill"))
        editor.press = AsyncMock()

        await client._set_editor_text(editor, "Direkt eingefügter Text")

        editor.press.assert_awaited_once_with("ControlOrMeta+A")
        page.keyboard.insert_text.assert_awaited_once_with("Direkt eingefügter Text")


if __name__ == "__main__":
    unittest.main()
