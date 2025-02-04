# ml-service/gbs_helper.py
import requests
import os
fromt dotenv import load_dotenv

load_dotenv()

GOOGLE_SAFE_BROWSING_API_KEY = os.getenv("GSB_API_KEY")

GSB_URL = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GOOGLE_SAFE_BROWSING_API_KEY}"

def check_google_safe_browsing(url: str) -> bool:
    """
    Retorna True se a URL for MALICIOSA segundo a Safe Browsing, ou False se for segura.
    """

    data = {
        "client": {
            "clientId": "phishdetector",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", 
                            "POTENTIALLY_HARMFUL_APPLICATION", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    try:
        resp = requests.post(GSB_URL, json=data)
        resp.raise_for_status()  # Lança exceção se status != 200
    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar Google Safe Browsing: {e}")
        return False

    # Se deu status 200
    result = resp.json()
    if "threatMatches" in result and len(result["threatMatches"]) > 0:
        return True
    
    return False
