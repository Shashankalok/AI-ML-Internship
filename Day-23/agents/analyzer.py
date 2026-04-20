from models.fraud_engine import run_fraud_engine
from tools.logger import log_info, log_error


def analyzer(state):
    """
    Analyzer Agent:
    Runs fraud detection engine and generates structured analysis
    """

    try:
        df = state.get("data")

        if df is None:
            raise ValueError("No data available for analysis")

        log_info("🧠 Running fraud detection engine")

        # Run ML + rules engine
        processed_df = run_fraud_engine(df)

        # -----------------------------
        # 📊 Safe Column Access
        # -----------------------------
        total = len(processed_df)

        fraud_cases = len(processed_df[processed_df.get("class", 0) == 1])

        anomaly_count = len(
            processed_df[processed_df.get("anomaly_flag", 0) == 1]
        )

        # -----------------------------
        # 📉 Risk Score
        # -----------------------------
        risk_score = round((fraud_cases / total) * 100, 4) if total else 0

        if risk_score > 2:
            risk_level = "HIGH"
        elif risk_score > 0.5:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        # -----------------------------
        # 📊 Behavioral Insights
        # -----------------------------
        fraud_df = processed_df[processed_df.get("class", 0) == 1]
        normal_df = processed_df[processed_df.get("class", 0) == 0]

        fraud_avg = round(fraud_df["amount"].mean(), 2) if not fraud_df.empty else 0
        normal_avg = round(normal_df["amount"].mean(), 2) if not normal_df.empty else 0

        # -----------------------------
        # 🔍 High Risk Transactions
        # -----------------------------
        high_risk_txns = processed_df[
        processed_df["risk_level"] == "HIGH"
        ].sort_values(by="risk_score", ascending=False)[["amount", "risk_score", "explanations"]]

        high_risk_txns = (
            high_risk_txns.head(5)
            .rename(columns={
                "risk_score": "risk_score_txn",
                "explanations": "risk_reasons"
            })
            .to_dict(orient="records")
        )

        log_info("✅ Analysis completed successfully")

        # -----------------------------
        # 🧾 Final Output
        # -----------------------------
        return {
            "processed_data": processed_df,
            "analysis": {
                "total_transactions": total,
                "fraud_cases": fraud_cases,
                "anomalies_detected": anomaly_count,
                "risk_score": risk_score,
                "risk_level": risk_level,
                "insights": {
                    "fraud_vs_normal_avg_amount": {
                        "fraud_avg": fraud_avg,
                        "normal_avg": normal_avg
                    },
                    "high_risk_transactions": high_risk_txns
                }
            },
            "status": "analyzed"
        }

    except Exception as e:
        log_error(f"❌ Analyzer error: {str(e)}")

        return {
            "status": "error",
            "message": str(e)
        }