$ErrorActionPreference = 'Continue'

# Consume hook JSON from stdin
if ($input) {
    $null = $input | Out-Null
} else {
    try { $null = [Console]::In.ReadToEnd() } catch {}
}

$git = 'C:\Program Files\Git\bin\git.exe'
if (-not (Test-Path $git)) {
    $git = 'git'
}

$root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
Set-Location $root

if (-not (Test-Path (Join-Path $root '.git'))) {
    exit 0
}

$remote = & $git remote get-url origin 2>$null
if (-not $remote) {
    exit 0
}

& $git add -A
$status = & $git status --porcelain
if (-not $status) {
    exit 0
}

$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
& $git commit -m "Auto-sync: $timestamp"
& $git push -u origin HEAD 2>&1 | Out-Null
exit 0
