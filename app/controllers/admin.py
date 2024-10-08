from sqlalchemy.orm import Session

from app.core.security import get_password_hash

from app.models.user import User


class AdminController:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        return self.db.query(User).all()

    def get_user_admin(self):
        return self.db.query(User).filter(User.role == "admin").first()

    def get_user(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, username: str, password: str, role: str):
        if self.get_user(username):
            return None
        user = User(username=username, hashed_password=get_password_hash(password), role=role)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def change_password(self, username: str, password: str):
        user = self.get_user(username)
        if not user:
            return None
        user.hashed_password = get_password_hash(password)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, username: str):
        user = self.get_user(username)
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        return user
