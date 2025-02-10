# PhishDetector

Um sistema completo para detecção de phishing em URLs, combinando **Java (Spring Boot)** para o backend principal, **Python (FastAPI)** para a lógica de Machine Learning e heurísticas, e **React** para o frontend.  
Atualmente, o projeto conta com:

1. **Heurísticas Avançadas** para análise de URLs (palavras-chave, análise de domínio, TLD suspeitos, etc.).  
2. **Integração com Google Safe Browsing (GSB)** para verificar se o link está em listas maliciosas.  
3. **Modelo de Machine Learning** (scikit-learn) que, com base em features de URLs, retorna se há suspeita de phishing.  
4. **Exibição no Frontend** (React) com histórico de análises.

---

## Tecnologias Utilizadas

- **Backend (Java + Spring Boot)**  
  - `Java 17+` (ou 21, dependendo do seu ambiente)  
  - `Maven` para gerenciamento de dependências  

- **Microserviço Python (FastAPI)**  
  - `Python 3.10+`  
  - `FastAPI` para a API de predição (`uvicorn` para rodar o servidor)  
  - `scikit-learn` e `joblib` para o modelo ML  
  - `tldextract` para heurísticas de domínio  
  - Integração com **Google Safe Browsing**  

- **Frontend (React + Material-UI)**  
  - `Node.js 16+`  
  - `Create React App`  
  - Página onde o usuário insere uma URL e recebe se é phishing ou não, além de um **score** e **motivos** (heurísticas).
