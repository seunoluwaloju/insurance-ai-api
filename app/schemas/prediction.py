from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    age: int = Field(..., ge=0, le=120)
    bmi: float = Field(..., ge=10, le=80)
    smoker: bool
    region: str = Field(..., min_length=2, max_length=50)
    children: int = Field(..., ge=0, le=20)


class PredictionResponse(BaseModel):
    risk_score: float
    risk_level: str
    explanation: str