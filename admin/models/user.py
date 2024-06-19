from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from .. import db, bcrypt

class User(UserMixin, db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[db.DateTime] = mapped_column(db.DateTime, server_default=func.now(), nullable=False)

    def get_id(self):
        return self._id
    
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, plaintext_password):
        self.password_hash = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

    def verify_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password_hash, plaintext_password)