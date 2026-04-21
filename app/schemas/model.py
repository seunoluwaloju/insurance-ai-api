from pydantic import BaseModel

class ModelInfoResponse(BaseModel):
    model_name: str
    model_type: str
    version: str