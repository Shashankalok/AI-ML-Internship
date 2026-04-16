from fastapi import FastAPI, BackgroundTasks
from models.patient import Patient
from services.monitor import check_patient_status
from middleware.logger import log_requests
import asyncio
import time
from db.database import cursor

app = FastAPI()

#  Middleware
app.middleware("http")(log_requests)


# Single Patient Monitoring
@app.post("/monitor")
async def monitor_patient(patient: Patient):
    result = await check_patient_status(patient)
    return result


#  Multiple Patients (Concurrency)

@app.post("/monitor-multiple")
async def monitor_multiple(patients: list[Patient]):
    tasks = [check_patient_status(p) for p in patients]
    results = await asyncio.gather(*tasks)
    return results



#  Background Alert System

def send_alert(message: str):
    with open("alerts.txt", "a") as f:
        f.write(message + "\n")


@app.post("/monitor-alert")
async def monitor_with_alert(patient: Patient, background_tasks: BackgroundTasks):
    result = await check_patient_status(patient)

    # FIX: result is dict now
    if result["status"] == "CRITICAL":
        background_tasks.add_task(send_alert, f"{result['name']} is CRITICAL")

    return result



#  Timeout Handling

@app.get("/timeout-check")
async def timeout_check():
    try:
        await asyncio.wait_for(asyncio.sleep(5), timeout=2)
    except asyncio.TimeoutError:
        return {"error": "Monitoring timeout!"}



#  Sync vs Async Comparison

@app.get("/sync-monitor")
def sync_monitor():
    time.sleep(2)
    return {"msg": "Sync monitoring done"}


@app.get("/async-monitor")
async def async_monitor():
    await asyncio.sleep(2)
    return {"msg": "Async monitoring done"}



#  Patient History API
@app.get("/history")
def get_history():
    cursor.execute("SELECT * FROM patients ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "name": row[1],
            "heart_rate": row[2],
            "oxygen_level": row[3],
            "risk_score": row[4],
            "status": row[5],
            "timestamp": row[6]
        })

    return data