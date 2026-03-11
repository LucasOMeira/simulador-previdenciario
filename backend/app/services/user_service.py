from sqlalchemy.orm import Session

from app.models.users import User, UserRole
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db: Session, user: UserCreate) -> User:
    
    user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
        role=UserRole.STUDENT
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()