"""Transparent deterministic/probabilistic reference model for QPKI-SmartHome.
This is not a cryptographic implementation and does not perform ML-KEM/ML-DSA.
"""
from dataclasses import dataclass, asdict
import random
from config import (TRANSMITTED_BYTES, LINK_RATE_BPS, RAW_TRANSMISSION_MS,
    WIRELESS_OVERHEAD_MS, WIRELESS_COMPONENT_MS, MCU_COMPUTATION_MS,
    END_TO_END_MS, HANDSHAKE_ENERGY_MJ, AUTH_BYPASS_PROBABILITY,
    CERTIFICATE_SIZES, BATTERY_LOW_PERCENT, BATTERY_MEDIUM_PERCENT)

@dataclass
class PerformanceEstimate:
    transmitted_bytes: int
    link_rate_bps: int
    raw_transmission_ms: float
    wireless_overhead_ms: float
    wireless_component_ms: float
    mcu_computation_ms: float
    end_to_end_ms: float
    energy_mj: float
    provenance: str = "model estimate; not physical measurement"

class QPKISmartHomeReferenceModel:
    """Calculates manuscript-reported model outputs and illustrative policy choices."""
    def performance(self):
        raw = TRANSMITTED_BYTES * 8 / LINK_RATE_BPS * 1000.0
        wireless = raw + WIRELESS_OVERHEAD_MS
        return PerformanceEstimate(
            transmitted_bytes=TRANSMITTED_BYTES, link_rate_bps=LINK_RATE_BPS,
            raw_transmission_ms=round(raw, 3), wireless_overhead_ms=WIRELESS_OVERHEAD_MS,
            wireless_component_ms=round(wireless, 3), mcu_computation_ms=MCU_COMPUTATION_MS,
            end_to_end_ms=round(wireless + MCU_COMPUTATION_MS, 3),
            energy_mj=HANDSHAKE_ENERGY_MJ)

    def certificate_size_table(self):
        return [dict(x, source="manuscript-reported; not re-measured from DER files") for x in CERTIFICATE_SIZES]

    def scheduler_choice(self, battery_percent: float):
        """Return a transparent illustrative parameter-set choice by battery state."""
        if not 0 <= battery_percent <= 100:
            raise ValueError("battery_percent must be between 0 and 100")
        if battery_percent < BATTERY_LOW_PERCENT:
            return {"battery_percent": battery_percent, "parameter_set": "ML-KEM-512", "reason": "low-battery illustrative policy"}
        if battery_percent < BATTERY_MEDIUM_PERCENT:
            return {"battery_percent": battery_percent, "parameter_set": "ML-KEM-768", "reason": "medium-battery illustrative policy"}
        return {"battery_percent": battery_percent, "parameter_set": "ML-KEM-1024", "reason": "high-battery illustrative policy"}

    def simulate_authentication(self, trials: int, seed: int):
        """Simulate the paper's random bypass abstraction; not an attack experiment."""
        if trials < 1: raise ValueError("trials must be >= 1")
        rng = random.Random(seed)
        rows=[]
        for i in range(trials):
            bypass = rng.random() < AUTH_BYPASS_PROBABILITY
            rows.append({"trial": i+1, "condition": "probabilistic_bypass_model",
                         "outcome": "bypass" if bypass else "accepted_as_expected",
                         "authentication_success": int(not bypass),
                         "bypass_probability_input": AUTH_BYPASS_PROBABILITY,
                         "source": "simulated model output; not an attack-harness result"})
        return rows
