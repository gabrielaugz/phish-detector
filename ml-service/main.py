# ml-service/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import uvicorn

from gbs_helper import check_google_safe_browsing

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECTOR_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

vectorizer = joblib.load(VECTOR_PATH)
clf = joblib.load(MODEL_PATH)

app = FastAPI()

class UrlItem(BaseModel):
    url: str

@app.post("/predict")
def predict_url(item: UrlItem):
    is_malicious_gsb = check_google_safe_browsing(item.url)

    X = vectorizer.transform([item.url])
    pred = clf.predict(X)
    ml_phishing = bool(pred[0] == 1)

    is_phishing = is_malicious_gsb or ml_phishing

    return {"phishing": is_phishing}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
