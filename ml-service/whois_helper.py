# ml-service/whois_helper.py
import whois
from datetime import datetime

def check_whois_info(domain: str) -> dict:
    """
    Retorna algumas informações relevantes do WHOIS sobre o domínio,
    ou um dicionário vazio se falhar.
    """
    try:
        w = whois.whois(domain)
        # creation_date, expiration_date, registrar, etc.
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        return {
            "creation_date": creation_date,
            "registrar": w.registrar,
            "country": w.country,
            "org": w.org
        }
    except:
        return {}