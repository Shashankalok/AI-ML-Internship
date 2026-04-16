from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    heart_rate: int
    oxygen_level: int