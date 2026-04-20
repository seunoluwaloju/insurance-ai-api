from fastapi import APIRouter
from app.schemas.prediction import PredictionRequest, PredictionResponse

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest) -> PredictionResponse:
    score = 0.78 if payload.smoker else 0.24
    level = "high" if score > 0.6 else "low"

    return PredictionResponse(
        risk_score=score,
        risk_level=level,
        explanation="Mock prediction based on smoker status for now"
    )