import json, urllib.request
from pathlib import Path
base = Path(__file__).resolve().parent
dest = base / 'evidence' / 'Ali_original_drafts_2026-10-15'
dest.mkdir(parents=True, exist_ok=True)
for item in json.loads((base / 'download_tasks.private.json').read_text(encoding='utf-8')):
    target = dest / item['name']
    if not target.exists() or target.stat().st_size != item['expected_size']:
        urllib.request.urlretrieve(item['url'], target)
    assert target.stat().st_size == item['expected_size'], item['name']
    print(item['name'], target.stat().st_size)
