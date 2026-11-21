$ErrorActionPreference = 'Stop'
$root = 'C:\Users\kmd37\Projects\vird'
$target = 'C:\Start-up'
$archive = Join-Path $target 'Patent_project_2026-10-21'
$dirs = @('docs\ali_submission','docs\ali_review_2026-10-13','docs\pbk_execution_2026-10-14','docs\pbk_act1_2026-10-15','docs\source\ppa7','assets\figures\ppa3456','assets\figures\ppa10')
$files = @($dirs | ForEach-Object { Get-ChildItem -LiteralPath (Join-Path $root $_) -Recurse -File } | Where-Object { $_.Extension -in '.pdf','.docx','.xlsx','.zip','.svg','.md','.txt' -and $_.FullName -notmatch '\\(extracted|word_qa|qa|__MACOSX)\\' -and $_.Name -notlike '._*' })
$files += @(Get-ChildItem -LiteralPath (Join-Path $root 'docs') -File | Where-Object { $_.Name -match '^(PPA|PATENT_|USPTO_PPA|MODULAR_CABINET_PATENT|ALI_MODULAR|PEREECHEN_DOKUMENTOV|POLNYJ_PERECHEN)' })
$files += Get-Item -LiteralPath (Join-Path $root 'NPPA1_Supplemental_Figures_EN.pdf'),(Join-Path $root 'outputs\patent_tracker\PATENT_ATTORNEYS_REGISTER_RU.xlsx'),(Join-Path $root 'docs\patent_attorney_tracker\data.json'),(Join-Path $root 'docs\patent_attorney_tracker\UPDATE_GUIDE_RU.md'),'C:\Users\kmd37\.cursor\projects\c-Users-kmd37-Projects-vird\canvases\patent-attorney-tracker.canvas.tsx'
$files = @($files | Sort-Object FullName -Unique)
$existing = @(Get-ChildItem -LiteralPath $target -Recurse -File)
$hashes = @{}
$manifest = @()
foreach ($file in $files) {
  $hash = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
  $found = $null
  foreach ($old in @($existing | Where-Object Length -eq $file.Length)) {
    if (-not $hashes.ContainsKey($old.FullName)) { $hashes[$old.FullName] = (Get-FileHash -LiteralPath $old.FullName -Algorithm SHA256).Hash }
    if ($hashes[$old.FullName] -eq $hash) { $found=$old.FullName; break }
  }
  if ($found) { $manifest += [pscustomobject]@{Status='Already present';Source=$file.FullName;Destination=$found;SHA256=$hash}; continue }
  if ($file.Name -eq 'PATENT_ATTORNEYS_REGISTER_RU.xlsx') { $dest=Join-Path $target $file.Name }
  elseif ($file.FullName.StartsWith($root+'\')) { $dest=Join-Path $archive $file.FullName.Substring($root.Length+1) }
  else { $dest=Join-Path $archive $file.Name }
  if (Test-Path -LiteralPath $dest) { $dest=Join-Path (Split-Path $dest) ($file.BaseName+'_'+$hash.Substring(0,8)+$file.Extension) }
  New-Item -ItemType Directory -Path (Split-Path $dest) -Force | Out-Null
  Copy-Item -LiteralPath $file.FullName -Destination $dest
  if ((Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash -ne $hash) { throw "Copy verification failed: $dest" }
  $manifest += [pscustomobject]@{Status='Copied';Source=$file.FullName;Destination=$dest;SHA256=$hash}
  $existing += Get-Item -LiteralPath $dest
  $hashes[$dest]=$hash
}
New-Item -ItemType Directory -Path $archive -Force | Out-Null
$manifest | Export-Csv -LiteralPath (Join-Path $archive 'COPY_MANIFEST.csv') -NoTypeInformation -Encoding utf8BOM
@('Архив документов патентного проекта PPA №1–10.','Вложенные папки сохраняют исходные имена и даты версий. Старые проекты не являются новыми документами для подписи.','Документы производства вагонов, рабочие программы и технические извлечения исключены.','COPY_MANIFEST.csv перечисляет скопированные файлы и найденные идентичные копии.','Таблица кандидатов: C:\Start-up\PATENT_ATTORNEYS_REGISTER_RU.xlsx') | Set-Content -LiteralPath (Join-Path $archive 'ПРОЧИТАТЬ.txt') -Encoding utf8
$manifest | Group-Object Status | Select-Object Name,Count | ConvertTo-Json
