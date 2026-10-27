"""Download official UCI 350 data with TLS and a checked file hash.

The hash pins the file retrieved during this project; it is not a publisher
signature. If the official release changes, inspect it rather than auto-repinning.
"""
import hashlib
import io
from pathlib import Path
import urllib.request
import zipfile

URL='https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip'
EXPECTED='30c6be3abd8dcfd3e6096c828bad8c2f011238620f5369220bd60cfc82700933'
path=Path(__file__).resolve().parent/'data/default_of_credit_card_clients.xls'
if path.exists():
    assert hashlib.sha256(path.read_bytes()).hexdigest()==EXPECTED, 'Existing data hash mismatch; inspect manually'
    print('Existing official dataset matches recorded SHA256.')
else:
    with urllib.request.urlopen(URL, timeout=60) as response:
        content=response.read()
    with zipfile.ZipFile(io.BytesIO(content)) as archive:
        matches=[n for n in archive.namelist() if n.endswith('.xls')]
        assert len(matches)==1, 'Unexpected archive layout'
        data=archive.read(matches[0])
    assert hashlib.sha256(data).hexdigest()==EXPECTED, 'Downloaded release differs; investigate before use'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(data)
    print('Official UCI data downloaded and hash checked.')
