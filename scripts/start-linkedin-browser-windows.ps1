$ErrorActionPreference = "Stop"

$browserCandidates = @(
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)

$browserPath = $browserCandidates | Where-Object { $_ -and (Test-Path $_) } | Select-Object -First 1
if (-not $browserPath) {
    throw "Weder Microsoft Edge noch Google Chrome wurde gefunden."
}

$profilePath = if ($env:LINKEDIN_BROWSER_PROFILE) {
    $env:LINKEDIN_BROWSER_PROFILE
} else {
    Join-Path $env:LOCALAPPDATA "linkedin-automation-browser"
}

New-Item -ItemType Directory -Force -Path $profilePath | Out-Null

$browserArguments = @(
    "--remote-debugging-port=9222",
    "--remote-debugging-address=0.0.0.0",
    "--user-data-dir=$profilePath",
    "--no-first-run",
    "--no-default-browser-check",
    "https://www.linkedin.com/feed/"
)

Start-Process -FilePath $browserPath -ArgumentList $browserArguments
Write-Host "LinkedIn-Browser gestartet: $browserPath"
Write-Host "Profil: $profilePath"

