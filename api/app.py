from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import uuid
import logging 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----- Models -----
class SensorData(BaseModel):
    temperature: float
    humidity: float
    lux: float
    motion: bool  # Match frontend field if needed

class UserSettings(BaseModel):
    user_temp: float
    user_light: str  # e.g. "18:30:00" or "sunset"
    light_duration: str  # e.g. "4h"

# ----- In-Memory Storage -----
latest_data: Optional[Dict] = None
settings_store: Dict = {}
data_log: List[Dict] = []

# ----- Helper Functions -----
def parse_duration(duration_str: str) -> timedelta:
    hours = int(duration_str.lower().replace("h", ""))
    return timedelta(hours=hours)

def get_sunset_time():
    # Fake sunset time for demo purposes
    return datetime.strptime("17:43:21", "%H:%M:%S").time()

def calculate_light_off(start_time_str: str, duration: str) -> str:
    start_time = datetime.strptime(start_time_str, "%H:%M:%S")
    off_time = start_time + parse_duration(duration)
    return off_time.strftime("%H:%M:%S")

# ----- Routes -----
@app.post("/update")
async def update_sensor_data(data: SensorData):
    global latest_data

    latest_data = {
        "temperature": data.temperature,
        "humidity": data.humidity,
        "lux": data.lux,
        "motion": data.motion,
        "timestamp": datetime.now().isoformat()
    }

    data_log.append({
        "temperature": data.temperature,
        "presence": data.motion,
        "datetime": latest_data["timestamp"]
    })

    print("Data received from ESP32:", latest_data)
    return {"message": "Sensor data received", "data": latest_data}

@app.get("/status")
async def get_status():
    if not latest_data:
        return {"message": "No data received yet"}

    user_temp = settings_store.get("user_temp")
    fan_status = "OFF"
    if user_temp is not None:
        fan_status = "ON" if latest_data["temperature"] > user_temp else "OFF"

    status = {
        "temperature": latest_data["temperature"],
        "humidity": latest_data["humidity"],
        "lux": latest_data["lux"],
        "motion": latest_data["motion"],
        "timestamp": latest_data["timestamp"],
        "fan": fan_status,
        "light": "ON" if latest_data["lux"] < 1000 or latest_data["motion"] else "OFF"
    }

    return {"message": "Current system status", "status": status}

@app.put("/settings")
async def update_settings(settings: UserSettings):
    try:
        _id = str(uuid.uuid4())

        if settings.user_light == "sunset":
            light_on_time = get_sunset_time().strftime("%H:%M:%S")
        else:
            datetime.strptime(settings.user_light, "%H:%M:%S")  # Validate format
            light_on_time = settings.user_light
            
        light_time_off = calculate_light_off(light_on_time, settings.light_duration)

        settings_store.update({
            "_id": _id,
            "user_temp": settings.user_temp,
            "user_light": light_on_time,
            "light_time_off": light_time_off
        })

        return {
            "_id": _id,
            "user_temp": settings.user_temp,
            "user_light": light_on_time,
            "light_time_off": light_time_off
        }
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/graph")
async def get_graph_data(size: int = Query(..., gt=0, le=100, description="Recent number of points (1-100)")):
    return data_log[-size:]
