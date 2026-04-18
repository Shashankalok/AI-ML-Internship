def apply_rules(row):
    rules = []

    if row.get("amount", 0) > 2000:
        rules.append("High transaction amount")

    if row.get("class", 0) == 1:
        rules.append("Known fraud pattern")

    if row.get("anomaly_flag", 0) == 1:
        rules.append("ML anomaly detected")

    return rules