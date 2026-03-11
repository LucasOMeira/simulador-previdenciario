from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.user_service import create_user, get_user_by_email
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    new_user = create_user(db, user)

    return {
        "id": new_user.id,
        "email": new_user.email,
        "message": "Usuário criado com sucesso"
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = get_user_by_email(db, user.email)

    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({
        "sub": str(db_user.id)
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }