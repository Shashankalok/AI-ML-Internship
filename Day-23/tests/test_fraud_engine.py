from tools.data_loader import load_data
from models.fraud_engine import run_fraud_engine


def test_fraud_engine():
    df = load_data("data/sample/creditcard.csv")

    processed = run_fraud_engine(df)

    assert "risk_score" in processed.columns
    assert "risk_level" in processed.columns
    assert "anomaly_flag" in processed.columns