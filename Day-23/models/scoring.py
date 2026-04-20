from config import Config


def calculate_risk_score(row):
    score = 0

    if row.get("anomaly_flag", 0) == 1:
        score += 50

    if row.get("class", 0) == 1:
        score += 30

    amount = row.get("amount", 0)

    if amount > 2000:
        score += 20
    elif amount > 1000:
        score += 10

    return min(score, 100)


def get_risk_level(score):
    if score >= Config.HIGH_RISK_THRESHOLD:
        return "HIGH"
    elif score >= Config.MEDIUM_RISK_THRESHOLD:
        return "MEDIUM"
    return "LOW"