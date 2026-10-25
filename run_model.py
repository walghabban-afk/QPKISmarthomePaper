"""Run the reproducible QPKI-SmartHome reference-model calculations."""
from dataclasses import asdict
from config import RESULTS_DIR, SIMULATION_TRIALS, RANDOM_SEED
from model import QPKISmartHomeReferenceModel
from utils import write_csv, write_json, save_performance_plot, save_confusion_matrix

def main():
    model=QPKISmartHomeReferenceModel()
    perf=model.performance()
    write_json(RESULTS_DIR/"performance_estimates.json",asdict(perf))
    write_csv(RESULTS_DIR/"certificate_sizes.csv",model.certificate_size_table())
    rows=model.simulate_authentication(SIMULATION_TRIALS,RANDOM_SEED)
    write_csv(RESULTS_DIR/"authentication_model_trials.csv",rows)
    successes=sum(r["authentication_success"] for r in rows)
    summary=[{"trials":len(rows),"successes":successes,"modelled_bypasses":len(rows)-successes,
              "observed_success_percent_in_this_simulation":round(100*successes/len(rows),4),
              "bypass_probability_input":0.003,
              "provenance":"seeded probabilistic model output; not measured reliability or attack test"}]
    write_csv(RESULTS_DIR/"authentication_model_summary.csv",summary)
    save_performance_plot(perf,RESULTS_DIR/"latency_model_estimates.png")
    save_confusion_matrix(rows,RESULTS_DIR/"authentication_outcome_counts.png")
    print("Performance model:")
    for k,v in asdict(perf).items(): print(f"  {k}: {v}")
    print(f"Authentication simulation: {successes}/{len(rows)} expected-acceptance outcomes (model only)")
    print(f"Outputs written to {RESULTS_DIR}")
if __name__=="__main__": main()
