"""Single-input inference for the scheduler reference policy, not ML prediction."""
import argparse, json
from model import QPKISmartHomeReferenceModel

def main():
    p=argparse.ArgumentParser(description="Query illustrative QPKI-SmartHome scheduler policy")
    p.add_argument("--battery",type=float,required=True,help="Battery percentage from 0 to 100")
    args=p.parse_args()
    print(json.dumps(QPKISmartHomeReferenceModel().scheduler_choice(args.battery),indent=2))
if __name__=="__main__": main()
