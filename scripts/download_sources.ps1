$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Raw = Join-Path $Root "raw_data"
New-Item -ItemType Directory -Force -Path $Raw | Out-Null

Write-Host "Downloading official/reference food-composition sources..."

Invoke-WebRequest `
  -Uri "https://www.nin.res.in/ebooks/IFCT2017.pdf" `
  -OutFile (Join-Path $Raw "IFCT2017.pdf")

Write-Host "IFCT 2017 downloaded."
Write-Host "Pakistan food-composition resources should be obtained from:" 
Write-Host "https://www.fao.org/infoods/infoods/tables-and-databases/pakistan/en/"
Write-Host "Official source files are intentionally not committed to Git. Check their applicable terms before redistribution."
