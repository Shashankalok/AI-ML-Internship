from tools.logger import log_info, log_error


def generate_report(state):
    """
    Writer Agent:
    Generates human-readable report + structured JSON output
    """

    try:
        analysis = state.get("analysis", {})

        if not analysis:
            log_error("❌ No analysis available for report generation")
            return {
                "final_output": "❌ No analysis available",
                "report_json": {}
            }

        log_info("📝 Generating final report")

        # -----------------------------
        #  Safe Extraction
        # -----------------------------
        total = analysis.get("total_transactions", 0)
        fraud = analysis.get("fraud_cases", 0)
        anomalies = analysis.get("anomalies_detected", 0)
        risk_score = round(analysis.get("risk_score", 0), 4)
        risk_level = analysis.get("risk_level", "UNKNOWN")

        insights = analysis.get("insights", {})

        fraud_avg = insights.get("fraud_vs_normal_avg_amount", {}).get("fraud_avg", 0)
        normal_avg = insights.get("fraud_vs_normal_avg_amount", {}).get("normal_avg", 0)

        high_risk_txns = insights.get("high_risk_transactions", [])

        # -----------------------------
        #  Executive Summary
        # -----------------------------
        if risk_level == "HIGH":
            summary = "High fraud risk detected. Immediate mitigation required."
        elif risk_level == "MEDIUM":
            summary = "Moderate fraud risk observed. Monitoring recommended."
        else:
            summary = "Low fraud risk with limited anomalies detected."

        # -----------------------------
        #  Derived Metrics
        # -----------------------------
        fraud_ratio = (fraud / total * 100) if total else 0
        anomaly_ratio = (anomalies / total * 100) if total else 0

        # -----------------------------
        #  High-Risk Transactions
        # -----------------------------
        txn_section = ""

        if high_risk_txns:
            for i, txn in enumerate(high_risk_txns[:5], 1):
                reasons = txn.get("risk_reasons", [])
                reasons_text = ", ".join(reasons) if reasons else "N/A"

                txn_section += f"""
{i}. Amount: {txn.get('amount', 'N/A')}
   Risk Score: {txn.get('risk_score_txn', 'N/A')}
   Reasons: {reasons_text}
"""
        else:
            txn_section = "No high-risk transactions identified."

        # -----------------------------
        #  Text Report
        # -----------------------------
        report_text = f"""
 FINANCIAL RISK INTELLIGENCE REPORT
====================================

 Executive Summary:
{summary}

 System Overview:
- Total Transactions: {total}
- Fraud Cases: {fraud}
- Anomalies Detected: {anomalies}

 Risk Metrics:
- Fraud Rate: {fraud_ratio:.4f}%
- Anomaly Rate: {anomaly_ratio:.4f}%
- Overall Risk Score: {risk_score}%
- Risk Level: {risk_level}

 Behavioral Insights:
- Avg Fraud Amount: {fraud_avg}
- Avg Normal Amount: {normal_avg}
- Fraud transactions are {'higher' if fraud_avg > normal_avg else 'lower'} in value

 High-Risk Transactions:
{txn_section}

 Observations:
- Hybrid ML + rule-based detection improves robustness
- Anomaly detection identifies hidden risk patterns
- Transaction-level scoring enables prioritization

 Recommendations:
- Monitor high-risk transactions in real-time
- Trigger alerts for risk score > 70
- Periodically retrain anomaly detection models

 Business Impact:
- Reduced financial loss exposure
- Improved fraud detection accuracy
- Better decision-making capability

====================================
""".strip()

        # -----------------------------
        # 🧾 JSON Output
        # -----------------------------
        report_json = {
            "summary": summary,
            "metrics": {
                "total_transactions": total,
                "fraud_cases": fraud,
                "anomalies": anomalies,
                "fraud_rate": round(fraud_ratio, 4),
                "anomaly_rate": round(anomaly_ratio, 4),
                "risk_score": risk_score,
                "risk_level": risk_level
            },
            "insights": {
                "fraud_avg_amount": fraud_avg,
                "normal_avg_amount": normal_avg,
                "high_risk_transactions": high_risk_txns[:5]
            },
            "recommendations": [
                "Enable real-time monitoring",
                "Set alerts for high-risk transactions",
                "Retrain anomaly detection periodically"
            ]
        }

        log_info(" Report generated successfully")

        return {
            "final_output": report_text,
            "report_json": report_json
        }

    except Exception as e:
        log_error(f" Writer error: {str(e)}")

        return {
            "final_output": " Report generation failed",
            "report_json": {}
        }