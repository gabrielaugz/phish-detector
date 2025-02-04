# ml-service/train_model.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def extract_features(urls):
    # Exemplo simples de extrair tokens (bag of words)
    # Em casos reais, parse de domínio, subdomínio, TLD, etc.
    vectorizer = CountVectorizer(token_pattern=r'[A-Za-z0-9]+')
    features = vectorizer.fit_transform(urls)
    return vectorizer, features

def main():
    # Pega o diretório base deste arquivo
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Monta caminhos para data e model
    DATA_PATH = os.path.join(BASE_DIR, "data", "phishing_dataset.csv")
    MODEL_DIR = os.path.join(BASE_DIR, "model")

    # 1. Carregar dataset
    # Verifique se phishing_dataset.csv existe em ml-service/data/
    df = pd.read_csv(DATA_PATH)  # Esperamos colunas: 'url' e 'label' (0 ou 1)

    urls = df['url'].astype(str).tolist()
    labels = df['label'].values

    # 2. Extrair features
    vectorizer, X = extract_features(urls)
    y = labels

    # 3. Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Treinar modelo
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # 5. Avaliar
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print("Acurácia:", acc)

    # 6. Salvar o pipeline (vectorizer + modelo) em ml-service/model/
    os.makedirs(MODEL_DIR, exist_ok=True)
    vector_path = os.path.join(MODEL_DIR, "vectorizer.pkl")
    model_path = os.path.join(MODEL_DIR, "model.pkl")

    joblib.dump(vectorizer, vector_path)
    joblib.dump(clf, model_path)

    print("Modelo salvo em:", model_path)
    print("Vectorizer salvo em:", vector_path)

if __name__ == "__main__":
    main()
