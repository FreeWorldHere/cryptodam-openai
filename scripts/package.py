"""Build or verify the portable plugin ZIP and both public copies, using only checked-in files."""
import argparse
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_STORED


def build(check):
    root = Path(__file__).resolve().parents[1]
    version = json.loads((root / 'plugin.json').read_text())['version']
    name = f'cryptodam-openai-plugin-{version}.zip'
    sources = [root / 'plugin.json', root / 'mcp.json', root / 'assets/logo.png']
    sources.extend(p for p in (root / 'skills').rglob('*') if p.is_file())
    memory = BytesIO()
    with ZipFile(memory, 'w', compression=ZIP_STORED) as archive:
        for path in sorted(sources):
            info = ZipInfo(path.relative_to(root).as_posix(), (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    content = memory.getvalue()
    checksum = f'{sha256(content).hexdigest()}  {name}\n'.encode()
    for directory in [root / 'downloads', root / 'site/downloads']:
        for path, data in [(directory / name, content), (directory / 'SHA256SUMS.txt', checksum)]:
            if check:
                if not path.is_file() or path.read_bytes() != data:
                    raise SystemExit(f'Stale package output: {path.relative_to(root)}')
            else:
                path.write_bytes(data)
    print(name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    build(parser.parse_args().check)
