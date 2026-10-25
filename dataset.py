"""Dataset note and optional scenario input loader.
QPKI-SmartHome is a design-and-modelling paper, not a dataset-trained ML paper.
No public dataset URL is claimed because the manuscript does not specify one.
"""
import csv
from pathlib import Path

def load_battery_scenarios(path=None):
    """Return a small illustrative set of battery inputs, or load a user CSV.

    A supplied CSV must contain one column named battery_percent. These are
    model inputs only and are not a dataset used to train or validate a model.
    """
    if path is None:
        return [{"battery_percent": x, "source": "illustrative input"} for x in (10, 35, 75, 95)]
    with Path(path).open(newline="",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    if not rows or "battery_percent" not in rows[0]:
        raise ValueError("CSV must contain a battery_percent column")
    return [{"battery_percent": float(r["battery_percent"]), "source": "user-provided scenario"} for r in rows]
