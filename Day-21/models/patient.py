from pydantic import BaseModel, Field, computed_field
from datetime import datetime

class Patient(BaseModel):
    name: str
    heart_rate: int = Field(..., ge=0, le=300)
    oxygen_level: int = Field(..., ge=0, le=100)


class PatientResponse(BaseModel):
    name: str
    heart_rate: int
    oxygen_level: int
    timestamp: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def status(self) -> str:
        if self.heart_rate >= 131 or self.heart_rate <= 40 or self.oxygen_level <= 88:
            return "CRITICAL"
        elif self.heart_rate >= 101 or self.oxygen_level <= 94:
            return "WARNING"
        return "STABLE"

    @computed_field
    @property
    def risk_score(self) -> int:
        score = 0

        # Heart rate scoring
        if self.heart_rate >= 131 or self.heart_rate <= 40:
            score += 5
        elif self.heart_rate >= 111:
            score += 3
        elif self.heart_rate >= 101:
            score += 1

        # Oxygen scoring
        if self.oxygen_level <= 88:
            score += 5
        elif self.oxygen_level <= 92:
            score += 3
        elif self.oxygen_level <= 94:
            score += 1

        return score