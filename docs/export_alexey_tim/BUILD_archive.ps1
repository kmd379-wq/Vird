# Собрать переписку Алексея Тим. → C:\Start-up\переписка с Алексеем Тим
param(
  [string[]]$SourceDirs = @(
    "C:\Start-up\переписка с Алексеем Тим",
    "C:\Start-up\переписка с Алексеем Тим\eml_gmail",
    "C:\Users\kmd37\Downloads",
    "C:\Users\kmd37\Desktop",
    "$PSScriptRoot\eml_gmail"
  ),
  [string]$Dest = "$PSScriptRoot\archive"
)

$DestEml = Join-Path $Dest "eml_gmail"
$DestAtt = Join-Path $Dest "attachments"
New-Item -ItemType Directory -Force -Path $DestEml, $DestAtt | Out-Null

$pattern = 'alexpbktech|nach@kvz39\.ru|ato@kvz39\.ru|kvz39\.ru'
$rows = [System.Collections.Generic.List[object]]::new()
$n = 0

function Test-EmlMatch([string]$path) {
  $head = Get-Content -LiteralPath $path -TotalCount 120 -Encoding UTF8 -ErrorAction SilentlyContinue
  if (-not $head) { $head = Get-Content -LiteralPath $path -TotalCount 120 -ErrorAction SilentlyContinue }
  $text = $head -join "`n"
  return ($text -match $pattern)
}

function Get-Header([string]$path, [string]$name) {
  $head = Get-Content -LiteralPath $path -TotalCount 80 -Encoding UTF8 -ErrorAction SilentlyContinue
  if (-not $head) { $head = Get-Content -LiteralPath $path -TotalCount 80 -ErrorAction SilentlyContinue }
  foreach ($line in $head) {
    if ($line -match "^(?i)$name\s*:\s*(.+)$") { return $matches[1].Trim() }
  }
  return ''
}

foreach ($dir in $SourceDirs) {
  if (-not (Test-Path $dir)) { continue }
  Get-ChildItem -LiteralPath $dir -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object { $_.Extension -eq '.eml' } |
    ForEach-Object {
      if (-not (Test-EmlMatch $_.FullName)) { return }
      $n++
      $destName = '{0:D4}_{1}' -f $n, $_.Name
      $target = Join-Path $DestEml $destName
      if ($_.FullName -ne $target) { Copy-Item -LiteralPath $_.FullName -Destination $target -Force }
      $rows.Add([pscustomobject]@{
        File = $destName
        Date = (Get-Header $target 'Date')
        From = (Get-Header $target 'From')
        To = (Get-Header $target 'To')
        Subject = (Get-Header $target 'Subject')
        Source = $_.FullName
      })
    }
}

$indexPath = Join-Path $Dest "INDEX_переписка_Алексей_Тим.csv"
$summaryPath = Join-Path $Dest "СВОДКА_переписка_RU.txt"
$rows | Sort-Object Date | Export-Csv $indexPath -Encoding UTF8 -NoTypeInformation

@"
Переписка с Алексеем Тим. (alexpbktech / nach@ / ato@ kvz39)
Собрано: $(Get-Date -Format 'yyyy-MM-dd HH:mm')
Писем в архиве: $($rows.Count)
Папка .eml: $DestEml

$(
  if ($rows.Count -eq 0) {
    'ПИСЬМА НЕ НАЙДЕНЫ. Положите .eml в eml_gmail и запустите скрипт снова.'
  } else {
    ($rows | ForEach-Object { "- $($_.Date) | $($_.From) | $($_.Subject)" }) -join "`n"
  }
)
"@ | Set-Content $summaryPath -Encoding UTF8

Write-Host "Copied $($rows.Count) messages -> $DestEml"
Write-Host "Index: $indexPath"