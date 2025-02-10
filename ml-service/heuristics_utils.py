# ml-service/heuristics_utils.py
import re
import tldextract

def score_heuristics(url: str) -> dict:
    url_lower = url.lower()
    score = 0
    reasons = []

    suspicious_keywords = {
        "phish": 30,
        "secure": 15,
        "login": 15,
        "verify": 15,
        "account": 15,
        "update": 15,
        "confirm": 15,
        "warning": 15,
        "alert": 15,
        "help": 15,
        "validation": 15,
        "client": 15,
        "manager": 15,
        "bank": 15,
        "checkout": 15,
        "verification": 15,
        "paypal": 15,
        "support": 15,
        "recover": 15,
        "locked": 15,
        "unlock": 15,
        "auth": 15,
        "signin": 15,
        "password": 15,
        "loans": 15,
        "win": 15
    }

    for kw, pts in suspicious_keywords.items():
        if kw in url_lower:
            score += pts
            reasons.append(f"Keyword '{kw}' encontrada (+{pts} pontos).")

    strange_patterns = ["@", "%00", "%2f%2f", "xn--"]
    for pattern in strange_patterns:
        if pattern in url_lower:
            score += 10
            reasons.append(f"Pattern suspeito '{pattern}' na URL (+10).")

    length_of_url = len(url)
    if length_of_url > 75:
        score += 5
        reasons.append("URL muito longa (>75 chars) (+5).")
    if length_of_url > 100:
        score += 5
        reasons.append("URL muito longa (>100 chars) (+5).")
    if length_of_url > 150:
        score += 10
        reasons.append("URL muito longa (>150 chars) (+10).")

    extracted = tldextract.extract(url_lower)
    subdomain = extracted.subdomain
    domain = extracted.domain
    suffix = extracted.suffix

    if re.match(r"^\d+$", domain):
        score += 20
        reasons.append("Domínio apenas dígitos (+20).")

    digits_in_domain = len(re.findall(r"\d", domain))
    if digits_in_domain >= 3:
        score += 5
        reasons.append("Domínio possui vários dígitos (+5).")

    subdomain_parts = subdomain.split(".")
    if len(subdomain_parts) > 2:
        score += 5
        reasons.append("Muitos subdomínios (+5).")

    suspicious_tlds = ["tk", "ga", "cf", "ml", "gq", "cn", "ru"]
    if suffix in suspicious_tlds:
        score += 10
        reasons.append(f"TLD suspeito: {suffix} (+10).")

    domain_suspicious_keywords = ["paypal", "google", "bank", "microsoft", "facebook"]
    for brand in domain_suspicious_keywords:
        if brand in domain or brand in subdomain:
            score += 10
            reasons.append(f"Brand '{brand}' no domínio/subdomínio (+10).")

    ip_pattern = r"(http[s]?://)?(\d{1,3}\.){3}\d{1,3}(:\d+)?"
    if re.match(ip_pattern, url_lower):
        score += 15
        reasons.append("URL contém IP no host (+15).")

    total_dashes = domain.count("-") + subdomain.count("-")
    if total_dashes >= 2:
        score += 5
        reasons.append("Muitos traços no domínio/subdomínio (+5).")

    if url_lower.startswith("http://"):
        score += 10
        reasons.append("Uso de HTTP, não HTTPS (+10).")

    if re.search(r"\.exe|\.apk|\.scr|\.zip", url_lower):
        score += 10
        reasons.append("Possível arquivo executável (exe/apk/scr/zip) (+10).")

    if ".com/" in url_lower:
        score += 10
        reasons.append("Uso suspeito de '.com/' no path (+10).")

    final_score = min(score, 100)
    return {
        "score": final_score,
        "reasons": reasons
    }