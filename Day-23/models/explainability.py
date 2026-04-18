def generate_explanation(row):
    explanations = []

    if row.get("anomaly_flag", 0) == 1:
        explanations.append("Deviation from normal transaction behavior")

    if row.get("class", 0) == 1:
        explanations.append("Matches known fraud pattern")

    if row.get("amount", 0) > 2000:
        explanations.append("Unusually high transaction amount")

    return explanations