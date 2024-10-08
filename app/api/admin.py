from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.router import router
from app.core.database import get_db
from app.core.security import decode_token
from app.api.auth import oauth2_scheme

from app.schemas.user import UserCreate, User

from app.controllers.admin import AdminController


@router.get("/admin")
async def read_admin(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    token_data = decode_token(token)
    if not token_data or token_data["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso não autorizado")
    return {"message": "Bem-vindo, administrador!"}


@router.get("/admin/users", response_model=list[User])
async def read_users(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    token_data = decode_token(token)
    if not token_data or token_data["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso não autorizado")
    return AdminController(db).get_users()


@router.post("/admin/users", response_model=User)
async def create_user(
        user: UserCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    token_data = decode_token(token)
    if not token_data or token_data["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso não autorizado")
    add_user = AdminController(db).create_user(user.username, user.password, user.role)
    if not add_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    return add_user


@router.patch("/admin/users/change/password/{username}", response_model=User)
async def change_password(
        username: str, password: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    token_data = decode_token(token)
    if not token_data or token_data["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso não autorizado")
    change_password = AdminController(db).change_password(username, password)
    if not change_password:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return change_password


@router.delete("/admin/users/{username}", response_model=User)
async def delete_user(
        username: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    token_data = decode_token(token)
    if not token_data or token_data["role"] != "admin":
        raise HTTPException(status_code=403, detail="Acesso não autorizado")
    delete_user = AdminController(db).delete_user(username)
    if not delete_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return delete_user
