from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.router import router
from app.core.database import get_db
from app.core.security import decode_token
from app.api.auth import oauth2_scheme


@router.get("/user")
async def read_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = decode_token(token)
    if not token_data:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    if token_data["role"] != "user":
        raise HTTPException(status_code=403, detail="Acesso não autorizado")
    return {"message": "Bem-vindo, usuário!"}
