# Экспорт alexpbktech / nach@ / ato@kvz39 из Outlook
$ErrorActionPreference = 'Continue'
$dest = $PSScriptRoot
$outDir = Join-Path $dest 'outlook_msg'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

function Test-MailMatch($m) {
  $from = [string]$m.SenderEmailAddress
  $to = [string]$m.To
  $body = [string]$m.Body
  return ($from -match 'alexpbktech|nach@kvz39|ato@kvz39' -or
          $to -match 'alexpbktech|nach@kvz39|ato@kvz39' -or
          $body -match 'alexpbktech|nach@kvz39|ato@kvz39')
}

$found = [System.Collections.Generic.List[object]]::new()
try {
  $ol = New-Object -ComObject Outlook.Application
  $ns = $ol.GetNamespace('MAPI')
  foreach ($fid in @(6, 5, 16, 3)) {
    try { $folder = $ns.GetDefaultFolder($fid) } catch { continue }
    for ($i = 1; $i -le $folder.Items.Count; $i++) {
      try {
        $m = $folder.Items.Item($i)
        if (-not (Test-MailMatch $m)) { continue }
        $safe = ($m.Subject -replace '[\\/:*?"<>|]', '_')
        if ($safe.Length -gt 50) { $safe = $safe.Substring(0, 50) }
        $fn = ('{0:yyyy-MM-dd_HH-mm}_{1}.msg' -f $m.ReceivedTime, $safe)
        $m.SaveAs((Join-Path $outDir $fn), 3)
        $found.Add([pscustomobject]@{
          Folder = $folder.Name; Subject = $m.Subject
          From = $m.SenderEmailAddress; To = $m.To
          Received = $m.ReceivedTime; File = $fn
        })
      } catch {}
    }
  }
} catch {
  Write-Warning "Outlook: $_"
  exit 1
}

Write-Host "Сохранено: $($found.Count) -> $outDir"
$found | Sort-Object Received -Descending | Export-Csv (Join-Path $dest 'INDEX_outlook.csv') -Encoding UTF8 -NoTypeInformation
$found | Format-Table -AutoSize