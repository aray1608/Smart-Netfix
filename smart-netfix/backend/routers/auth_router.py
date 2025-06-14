from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from backend.auth import verify_password, create_access_token
from backend.models import fake_admin

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    if data.username != fake_admin["username"] or not verify_password(data.password, fake_admin["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    token = create_access_token({"sub": data.username})
    return {"access_token": token, "token_type": "bearer"}
