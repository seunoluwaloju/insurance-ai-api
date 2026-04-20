from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import generate_api_key, hash_api_key, get_current_user
from app.db.models import User
from app.db.session import get_db
from app.schemas.auth import CreateApiKeyResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/create-api-key", response_model=CreateApiKeyResponse)
def create_api_key(db: Session = Depends(get_db)) -> CreateApiKeyResponse:
    api_key = generate_api_key()
    api_key_hash = hash_api_key(api_key)

    user = User(api_key_hash=api_key_hash)
    db.add(user)
    db.commit()

    return CreateApiKeyResponse(api_key=api_key)


@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)) -> dict:
    return {
        "id": current_user.id,
        "email": current_user.email,
    }