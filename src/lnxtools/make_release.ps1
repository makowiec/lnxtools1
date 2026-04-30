# ========================================
# make_release.ps1 - generator version.py
# ========================================

# Pobranie aktualnego taga
$version = git describe --tags 2>$null
if (-not $version) {
    $version = "no-tag"
}

# Pobranie skrotu commitu
$commit = git rev-parse --short HEAD 2>$null
if (-not $commit) {
    $commit = "no-commit"
}

# Pobranie nazwy galezi
$branch = git rev-parse --abbrev-ref HEAD 2>$null
if (-not $branch) {
    $branch = "no-branch"
}

Write-Host "Building version.py for version: $version ($commit) on branch $branch"

# Generowanie pliku version.py
@"
VERSION = "$version"
COMMIT = "$commit"
BRANCH = "$branch"
"@ | Out-File -Encoding UTF8 version.py

Write-Host "version.py generated successfully."