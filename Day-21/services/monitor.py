import asyncio
from models.patient import PatientResponse
from db.database import cursor, conn
from ml.model import predict_risk

async def check_patient_status(patient):
    await asyncio.sleep(0.1)

    # -----------------------------
    #  Create Response Object
    # -----------------------------
    result = PatientResponse(
        name=patient.name,
        heart_rate=patient.heart_rate,
        oxygen_level=patient.oxygen_level
    )

    # -----------------------------
    #  ML Prediction
    # -----------------------------
    ml_output = predict_risk(
        patient.heart_rate,
        patient.oxygen_level
    )

    # -----------------------------
    #  Save to Database
    # -----------------------------
    cursor.execute(
        """INSERT INTO patients 
        (name, heart_rate, oxygen_level, risk_score, status, timestamp) 
        VALUES (?, ?, ?, ?, ?, ?)""",
        (
            result.name,
            result.heart_rate,
            result.oxygen_level,
            result.risk_score,
            result.status,
            str(result.timestamp)
        )
    )
    conn.commit()

    # -----------------------------
    #  Return Final Output
    # -----------------------------
    return {
        "name": result.name,
        "heart_rate": result.heart_rate,
        "oxygen_level": result.oxygen_level,
        "risk_score": result.risk_score,
        "status": result.status,
        "timestamp": str(result.timestamp),
        "ml_prediction": ml_output["prediction"],
        "confidence": ml_output["confidence"]
    }