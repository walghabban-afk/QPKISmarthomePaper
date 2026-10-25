# Reproducibility audit

## Verified in this archive

- The shipped unit tests check transmission arithmetic, end-to-end component arithmetic, manuscript-reported certificate-size input values, scheduler input bounds, and seeded simulation reproducibility.
- The seeded authentication simulation contains 15,000 generated trial rows plus a CSV header. These are model draws and are not attack-harness observations.
- `results/certificate_sizes.csv` explicitly marks certificate sizes as manuscript-reported and not re-measured from DER files.
- The manifest is regenerated from the final files and excludes itself. Python bytecode/cache files are not shipped.

## Not verified / not included

- No certificate fixtures, encoder/decoder implementation, or certificate round-trip SHA-256 test. Consequently the manuscript's 5,627 B to 5,342 B certificate-size comparison is not reproduced by this archive.
- No cryptographic handshake implementation, attack harness, dataset-driven evaluation, cloud-scale simulation, or physical hardware measurements.
- No complete formal security proof for an implemented protocol. The manuscript's security discussion is conditional and should be read as a set of proof obligations.

## Rebuild checksums

From the repository root, regenerate the manifest with:

```bash
python - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
manifest = root / 'MANIFEST.sha256'
files = sorted(p for p in root.rglob('*') if p.is_file() and p != manifest and '__pycache__' not in p.parts)
manifest.write_text(''.join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.as_posix()}\n" for p in files), encoding='utf-8')
PY
sha256sum -c MANIFEST.sha256
python -m unittest discover -s tests -v
```
