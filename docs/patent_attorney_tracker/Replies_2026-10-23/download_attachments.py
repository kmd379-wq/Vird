import json, urllib.request
from pathlib import Path
B=Path(__file__).resolve().parent
for item in json.loads((B/'download_tasks.private.json').read_text(encoding='utf-8')):
    dest=B/item['name']
    if not dest.exists() or dest.stat().st_size!=item['expected_size']:
        urllib.request.urlretrieve(item['url'],dest)
    assert dest.stat().st_size==item['expected_size']
    print(item['name'],dest.stat().st_size)
