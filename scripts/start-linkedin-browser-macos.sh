#!/usr/bin/env bash
set -euo pipefail

edge_path="/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
chrome_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
profile_path="${LINKEDIN_BROWSER_PROFILE:-$HOME/linkedin-automation-browser}"

if [[ -x "$edge_path" ]]; then
  browser_path="$edge_path"
elif [[ -x "$chrome_path" ]]; then
  browser_path="$chrome_path"
else
  echo "Weder Microsoft Edge noch Google Chrome wurde unter /Applications gefunden." >&2
  exit 1
fi

mkdir -p "$profile_path"

exec "$browser_path" \
  --remote-debugging-port=9222 \
  --remote-debugging-address=0.0.0.0 \
  --user-data-dir="$profile_path" \
  --no-first-run \
  --no-default-browser-check \
  "https://www.linkedin.com/feed/"

