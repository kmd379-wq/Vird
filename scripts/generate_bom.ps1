# Generate MVP_BOM_v1.xlsx from data/mvp_bom_v1.json via Excel COM
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$jsonPath = Join-Path $root 'data\mvp_bom_v1.json'
$outPath = Join-Path $root 'docs\MVP_BOM_v1.xlsx'

$data = Get-Content -Path $jsonPath -Raw -Encoding UTF8 | ConvertFrom-Json
$headers = $data.headers
$rows = $data.rows

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

if (Test-Path $outPath) { Remove-Item $outPath -Force }
$wb = $excel.Workbooks.Add()
while ($wb.Worksheets.Count -gt 1) { $wb.Worksheets.Item($wb.Worksheets.Count).Delete() }

function Set-HeaderRow($sheet, $cols) {
    for ($c = 0; $c -lt $cols.Count; $c++) {
        $cell = $sheet.Cells.Item(1, $c + 1)
        $cell.Value2 = $cols[$c]
        $cell.Font.Bold = $true
        $cell.Interior.Color = 0x4D4D1F
        $cell.Font.Color = 0xFFFFFF
    }
    $sheet.Rows.Item(1).WrapText = $true
}

# --- BOM sheet ---
$ws = $wb.Worksheets.Item(1)
$ws.Name = 'BOM'
Set-HeaderRow $ws $headers
$ws.Cells.Item(1, 14).Value2 = 'Line USD'
$ws.Cells.Item(1, 14).Font.Bold = $true
$ws.Cells.Item(1, 14).Interior.Color = 0x4D4D1F
$ws.Cells.Item(1, 14).Font.Color = 0xFFFFFF

$total = 0.0
$mustTotal = 0.0
$prevCat = ''
$r = 2

foreach ($row in $rows) {
    $qty = [double]$row[5]
    $price = [double]$row[10]
    $line = $qty * $price
    $total += $line
    if ($row[7] -eq 'Must') { $mustTotal += $line }

    for ($c = 0; $c -lt 13; $c++) {
        $val = $row[$c]
        if ($c -eq 5 -or $c -eq 10) {
            $ws.Cells.Item($r, $c + 1).Value2 = [double]$val
        } else {
            $ws.Cells.Item($r, $c + 1).Value2 = [string]$val
        }
    }
    $ws.Cells.Item($r, 14).Value2 = [double]$line

    if ($row[0] -ne $prevCat) {
        $ws.Range($ws.Cells.Item($r,1), $ws.Cells.Item($r,14)).Interior.Color = 0xF0F0E8
        $prevCat = $row[0]
    } elseif ($row[7] -eq 'Optional') {
        $ws.Range($ws.Cells.Item($r,1), $ws.Cells.Item($r,14)).Interior.Color = 0xE8F8FF
    }
    $r++
}

$tr = $r + 1
$ws.Cells.Item($tr, 12).Value2 = 'TOTAL all lines'
$ws.Cells.Item($tr, 12).Font.Bold = $true
$ws.Cells.Item($tr, 14).Value2 = [double]$total
$ws.Cells.Item($tr, 14).Font.Bold = $true
$ws.Cells.Item($tr + 1, 12).Value2 = 'TOTAL Must only'
$ws.Cells.Item($tr + 1, 12).Font.Bold = $true
$ws.Cells.Item($tr + 1, 14).Value2 = [double]$mustTotal
$ws.Cells.Item($tr + 1, 14).Font.Bold = $true

$ws.Columns.AutoFit() | Out-Null
try {
    $ws.Range("K2:K$r").NumberFormat = '0.00'
    $ws.Range("N2:N$r").NumberFormat = '0.00'
    $ws.Range("N$tr`:N$($tr+1)").NumberFormat = '0.00'
} catch { }
$ws.Application.ActiveWindow.SplitRow = 1
$ws.Application.ActiveWindow.FreezePanes = $true

# --- Summary by category ---
$ws2 = $wb.Worksheets.Add([Type]::Missing, $ws)
$ws2.Name = 'Summary'
Set-HeaderRow $ws2 @('Category', 'Items', 'Sum USD', 'Must USD')

$catMap = @{}
foreach ($row in $rows) {
    $cat = $row[0]
    $line = [double]$row[5] * [double]$row[10]
    if (-not $catMap.ContainsKey($cat)) { $catMap[$cat] = @{ count = 0; sum = 0.0; must = 0.0 } }
    $catMap[$cat].count++
    $catMap[$cat].sum += $line
    if ($row[7] -eq 'Must') { $catMap[$cat].must += $line }
}
$sr = 2
foreach ($cat in ($catMap.Keys | Sort-Object)) {
    $ws2.Cells.Item($sr, 1).Value2 = [string]$cat
    $ws2.Cells.Item($sr, 2).Value2 = [double]$catMap[$cat].count
    $ws2.Cells.Item($sr, 3).Value2 = [double]$catMap[$cat].sum
    $ws2.Cells.Item($sr, 4).Value2 = [double]$catMap[$cat].must
    $sr++
}
$ws2.Cells.Item($sr + 1, 1).Value2 = 'TOTAL'
$ws2.Cells.Item($sr + 1, 1).Font.Bold = $true
$ws2.Cells.Item($sr + 1, 2).Value2 = [double](($catMap.Values | ForEach-Object { $_.count } | Measure-Object -Sum).Sum)
$ws2.Cells.Item($sr + 1, 3).Value2 = [double]$total
$ws2.Cells.Item($sr + 1, 4).Value2 = [double]$mustTotal
$ws2.Columns.AutoFit() | Out-Null

# --- By module ---
$ws3 = $wb.Worksheets.Add([Type]::Missing, $ws2)
$ws3.Name = 'By Module'
Set-HeaderRow $ws3 @('Module', 'Items', 'Sum USD')

$modMap = @{}
foreach ($row in $rows) {
    $mod = $row[4]
    $line = [double]$row[5] * [double]$row[10]
    if (-not $modMap.ContainsKey($mod)) { $modMap[$mod] = @{ count = 0; sum = 0.0 } }
    $modMap[$mod].count++
    $modMap[$mod].sum += $line
}
$mr = 2
foreach ($mod in ($modMap.Keys | Sort-Object)) {
    $ws3.Cells.Item($mr, 1).Value2 = [string]$mod
    $ws3.Cells.Item($mr, 2).Value2 = [double]$modMap[$mod].count
    $ws3.Cells.Item($mr, 3).Value2 = [double]$modMap[$mod].sum
    $mr++
}
$ws3.Columns.AutoFit() | Out-Null

# --- Meta ---
$ws4 = $wb.Worksheets.Add([Type]::Missing, $ws3)
$ws4.Name = 'Meta'
$m = $data.meta
$ws4.Cells.Item(1, 1).Value2 = 'Document'
$ws4.Cells.Item(1, 2).Value2 = $m.document
$ws4.Cells.Item(2, 1).Value2 = 'Version'
$ws4.Cells.Item(2, 2).Value2 = $m.version
$ws4.Cells.Item(3, 1).Value2 = 'Date'
$ws4.Cells.Item(3, 2).Value2 = $m.date
$ws4.Cells.Item(4, 1).Value2 = 'Project'
$ws4.Cells.Item(4, 2).Value2 = $m.project
$ws4.Cells.Item(5, 1).Value2 = 'Market'
$ws4.Cells.Item(5, 2).Value2 = $m.market
$ws4.Cells.Item(6, 1).Value2 = 'Base TZ'
$ws4.Cells.Item(6, 2).Value2 = $m.baseTz
$ws4.Cells.Item(7, 1).Value2 = 'Currency'
$ws4.Cells.Item(7, 2).Value2 = $m.currency
$nr = 9
foreach ($note in $m.notes) {
    $ws4.Cells.Item($nr, 1).Value2 = "Note"
    $ws4.Cells.Item($nr, 2).Value2 = $note
    $nr++
}
$ws4.Cells.Item($nr + 1, 1).Value2 = 'TOTAL all USD'
$ws4.Cells.Item($nr + 1, 2).Value2 = [double][math]::Round($total, 2)
$ws4.Cells.Item($nr + 2, 1).Value2 = 'TOTAL Must USD'
$ws4.Cells.Item($nr + 2, 2).Value2 = [double][math]::Round($mustTotal, 2)
$ws4.Columns.Item(1).ColumnWidth = 16
$ws4.Columns.Item(2).ColumnWidth = 55

$docsDir = Split-Path $outPath -Parent
if (-not (Test-Path $docsDir)) { New-Item -ItemType Directory -Path $docsDir -Force | Out-Null }

$wb.SaveAs($outPath)
$wb.Close($false)
$excel.Quit()
[GC]::Collect()

Write-Output "Saved: $outPath"
Write-Output ("Total: {0:N2} USD | Must: {1:N2} USD" -f $total, $mustTotal)
