from pydantic import BaseModel

class PredictionRequest(BaseModel):
    age: int
    bmi: float
    smoker: bool
    region: str
    children: int

class PredictionResponse(BaseModel):
    risk_score: float
    risk_level: str
    explanation: str