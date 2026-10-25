"""Configuration values transcribed from the QPKI-SmartHome revised manuscript.
Section references are approximate manuscript section labels; values are model inputs,
not physical-device measurements. See README.md before interpreting results.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"
CHECKPOINT_DIR = ROOT / "checkpoints"
FIGURES_DIR = ROOT / "figures"

PAPER_TITLE = "QPKI-SmartHome: Post-Quantum Public Key Infrastructure with Lightweight Lattice-Based Authentication for Cloud-Tethered IoT Smart Home Devices"
TARGET_MCU = "ARM Cortex-M4 target (STM32F429ZI stated in manuscript)"
MCU_CLOCK_MHZ = 168
DEVICE_FLASH_KB = 2048
DEVICE_RAM_KB_CONTEXT = 256

# Section 6.3 / model configuration: model inputs, not instrumented measurements.
TRANSMITTED_BYTES = 14232
LINK_RATE_BPS = 250_000
RAW_TRANSMISSION_MS = TRANSMITTED_BYTES * 8 / LINK_RATE_BPS * 1000.0
WIRELESS_OVERHEAD_MS = 52.176  # modelled protocol/framing overhead to match reported wireless component
WIRELESS_COMPONENT_MS = RAW_TRANSMISSION_MS + WIRELESS_OVERHEAD_MS
MCU_COMPUTATION_MS = 38.0
END_TO_END_MS = WIRELESS_COMPONENT_MS + MCU_COMPUTATION_MS
HANDSHAKE_ENERGY_MJ = 4.75

# Table 8: manuscript-reported certificate-size values retained as inputs only.
# This package contains no DER fixtures or encoder/decoder and does not reproduce
# these values or verify round-trip reconstruction.
CERTIFICATE_SIZES = [
    {"certificate_type": "ML-DSA-44", "full_der_bytes": 4098, "delta_encoded_bytes": 3813, "irreducible_floor_bytes": None, "reduction_percent": 7.0},
    {"certificate_type": "ML-DSA-65", "full_der_bytes": 5627, "delta_encoded_bytes": 5342, "irreducible_floor_bytes": 5261, "reduction_percent": 5.1},
    {"certificate_type": "ML-DSA-87", "full_der_bytes": 7585, "delta_encoded_bytes": 7300, "irreducible_floor_bytes": None, "reduction_percent": 3.8},
    {"certificate_type": "Full chain", "full_der_bytes": 17310, "delta_encoded_bytes": 16873, "irreducible_floor_bytes": None, "reduction_percent": 2.5},
]

# Section 6.8: model-only per-handshake bypass probability. Not an attack harness.
AUTH_BYPASS_PROBABILITY = 0.003
SIMULATION_TRIALS = 15000
RANDOM_SEED = 20261023

# Illustrative scheduler thresholds. They are a reference-model policy, not a trained model.
BATTERY_LOW_PERCENT = 20
BATTERY_MEDIUM_PERCENT = 50
