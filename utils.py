"""Output helpers for the QPKI-SmartHome reference model."""
import csv, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def write_csv(path, rows):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    if not rows: return
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def write_json(path, data):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,indent=2),encoding="utf-8")

def save_performance_plot(perf, out):
    labels=["Raw transmission", "Wireless component", "MCU computation", "End-to-end"]
    values=[perf.raw_transmission_ms,perf.wireless_component_ms,perf.mcu_computation_ms,perf.end_to_end_ms]
    fig,ax=plt.subplots(figsize=(8,4.5)); bars=ax.bar(labels,values)
    ax.set_ylabel("Latency (ms)"); ax.set_title("QPKI-SmartHome model estimates (not physical measurements)")
    ax.tick_params(axis="x",rotation=15)
    for b,v in zip(bars,values): ax.text(b.get_x()+b.get_width()/2,b.get_height(),f"{v:.1f}",ha="center",va="bottom")
    fig.tight_layout(); Path(out).parent.mkdir(parents=True,exist_ok=True); fig.savefig(out,dpi=300); plt.close(fig)

def save_confusion_matrix(success, out):
    # Matrix represents the two outcomes of the probabilistic model only.
    failures=len(success)-sum(int(r["authentication_success"]) for r in success)
    counts=[[sum(int(r["authentication_success"]) for r in success), failures]]
    fig,ax=plt.subplots(figsize=(5,2.5)); im=ax.imshow(counts,aspect="auto")
    ax.set_xticks([0,1],labels=["Expected acceptance", "Modelled bypass"]); ax.set_yticks([0],labels=["All trials"])
    for j,v in enumerate(counts[0]): ax.text(j,0,str(v),ha="center",va="center")
    ax.set_title("Outcome counts — probabilistic model, not attack evaluation")
    fig.colorbar(im,ax=ax); fig.tight_layout(); Path(out).parent.mkdir(parents=True,exist_ok=True); fig.savefig(out,dpi=300); plt.close(fig)
