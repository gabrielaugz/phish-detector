# ml-service/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

from heuristics_utils import score_heuristics
from gbs_helper import check_google_safe_browsing

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")

clf = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

class UrlItem(BaseModel):
    url: str

# new idea for "phish or not"
# score system added
@app.post("/predict")
def predict_url(item: UrlItem):
    url = item.url
    
    heur = score_heuristics(url)
    heur_score = heur["score"]

    gsb_malicious = bool(check_google_safe_browsing(url))

    X = vectorizer.transform([url])  
    ml_pred_np = clf.predict(X)[0]   # 1=phishing
    ml_pred = int(ml_pred_np)        # native int

    is_phishing = (heur_score >= 20) or gsb_malicious or (ml_pred == 1)
    is_phishing = bool(is_phishing)

    return {
        "url": url,
        "phishing": is_phishing,
        "score": int(heur_score),
        "reasons": heur["reasons"],
        "gsb": gsb_malicious,
        "ml_pred": ml_pred
    }

