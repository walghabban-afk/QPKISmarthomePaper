# QPKI-SmartHome Reference Model and Figure Archive

**Paper:** QPKI-SmartHome: Post-Quantum Public Key Infrastructure with Lightweight Lattice-Based Authentication for Cloud-Tethered IoT Smart Home Devices  
**Package type:** Executable arithmetic/probabilistic reference model; not a production cryptographic implementation.

## Scope and limitations

This repository reproduces selected arithmetic and seeded probabilistic outputs described in the manuscript. It is not firmware, a cryptographic library, a trained machine-learning model, a complete handshake implementation, or a hardware benchmark suite.

- Latency, energy, and peak-RAM figures are configured model estimates, not physical measurements.
- The certificate-size values in `results/certificate_sizes.csv` are transcribed from the manuscript. No DER certificate fixtures or executable certificate encoder/decoder are included, so the reported reductions are **not independently reproduced** by this package. No certificate round-trip or SHA-256 reconstruction test is included.
- Authentication trials are seeded draws from a configured per-handshake bypass-probability abstraction. They are not packet-injection, replay, MITM, or other attack-harness experiments. The released CSV contains 15,000 generated trial rows; this count is a simulation count only, not an empirical attack sample.
- No cloud-side scalability simulation, database schema, firmware, linker map, packet captures, hardware traces, CA private keys, or deployed Zstandard dictionary is included.
- The scheduler is an illustrative policy mapping, not a trained ML predictor or a cryptographic security parameter negotiation implementation.
- The manuscript's security section is an analytical outline/conditional proof target, not a completed formal proof for an implemented protocol.

## Key model values

| Quantity | Value | Interpretation |
|---|---:|---|
| Transmitted bytes | 14,232 B | configured model input |
| Link rate | 250,000 bit/s | stated wireless assumption |
| Raw transmission | 455.424 ms | calculated as bytes × 8 / bit rate |
| Wireless overhead | 52.176 ms | configured model input |
| Wireless component | 507.600 ms | raw transmission plus configured overhead |
| MCU cryptographic computation | 38.0 ms | model input/estimate |
| End-to-end latency | 545.600 ms | wireless component + MCU computation |
| Handshake energy | 4.75 mJ | model estimate/configured value |
| ML-DSA-65 full/delta size | 5,627 / 5,342 B | manuscript-reported; not reproduced by package |
| Bypass probability | 0.003 per handshake | stochastic model input, not empirical attack probability |

The arithmetic for the model values can be checked with the included tests. The certificate-size figures are provenance-labelled inputs only.

## Installation

Python 3.10–3.12 is recommended. Create a virtual environment, then run:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the reference model

```bash
python run_model.py
python evaluate.py
python inference.py --battery 35
python -m unittest discover -s tests -v
```

`run_model.py` generates performance estimates, certificate-size input CSV, seeded simulation trials/summary, and plots. `train.py` intentionally does not train a model because no ML dataset or neural architecture is specified in the manuscript. `data/download_data.py` does not download a dataset for the same reason.

## Repository contents

- `config.py`, `model.py`, `utils.py`: configured inputs and reference calculations.
- `run_model.py`, `evaluate.py`, `inference.py`: model entry points.
- `tests/`: unit tests for arithmetic, configured input provenance, scheduler bounds, and seeded reproducibility.
- `results/`: generated model outputs; not hardware/attack measurements.
- `figures/`: manuscript images extracted at original resolution and table renders for reference.
- `SOURCE_MANUSCRIPT.txt`: identifies the manuscript source used to build this archive.
- `MANIFEST.sha256`: SHA-256 checksums for all shipped files except the manifest itself.
- `LICENSE`: Creative Commons Attribution 4.0 International for this reference package, subject to third-party assets remaining under their respective rights.

## Security note

This package does not implement ML-KEM, ML-DSA, X.509 parsing, production certificate compression, or a complete handshake. It must not be used as a security-critical implementation. Use vetted cryptographic libraries and an independently reviewed protocol implementation.
