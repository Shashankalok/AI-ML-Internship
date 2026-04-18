from models.anomaly_detection import run_anomaly_detection
from models.scoring import calculate_risk_score, get_risk_level
from models.fraud_rules import apply_rules
from models.explainability import generate_explanation


def run_fraud_engine(df):

    #  1: ML anomaly detection
    df = run_anomaly_detection(df)

    # 2: Risk scoring
    df["risk_score"] = df.apply(calculate_risk_score, axis=1)

    #  3: Risk level
    df["risk_level"] = df["risk_score"].apply(get_risk_level)

    # 4 : Rules
    df["rules_triggered"] = df.apply(apply_rules, axis=1)

    # 5 : Explainability
    df["explanations"] = df.apply(generate_explanation, axis=1)

    return df