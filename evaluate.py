"""Summarize configured model outputs; no empirical test set exists in the paper."""
import csv
from pathlib import Path
from config import RESULTS_DIR
from run_model import main as generate

def main():
    generate()
    with (RESULTS_DIR/"authentication_model_summary.csv").open(newline="",encoding="utf-8") as f:
        row=next(csv.DictReader(f))
    print("
Model-output summary (not empirical evaluation)")
    for k,v in row.items(): print(f"{k}: {v}")
    print("No ROC/AUC, F1, precision/recall, or dataset metrics are reported: the paper defines no labelled test dataset or classifier.")
if __name__=="__main__": main()
