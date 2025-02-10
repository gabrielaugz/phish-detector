# ml-service/train_model.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def extract_features(urls):
    vectorizer = CountVectorizer(token_pattern=r'[A-Za-z0-9]+')
    features = vectorizer.fit_transform(urls)
    return vectorizer, features

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    DATA_PATH = os.path.join(BASE_DIR, "data", "phishing_dataset.csv")
    MODEL_DIR = os.path.join(BASE_DIR, "model")

    df = pd.read_csv(DATA_PATH)  # columns: 'url' and 'label'

    urls = df['url'].astype(str).tolist()
    labels = df['label'].values

    vectorizer, X = extract_features(urls)
    y = labels

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print("Acurácia:", acc)

    os.makedirs(MODEL_DIR, exist_ok=True)
    vector_path = os.path.join(MODEL_DIR, "vectorizer.pkl")
    model_path = os.path.join(MODEL_DIR, "model.pkl")

    joblib.dump(vectorizer, vector_path)
    joblib.dump(clf, model_path)

    print("Modelo salvo em:", model_path)
    print("Vectorizer salvo em:", vector_path)

if __name__ == "__main__":
    main()
