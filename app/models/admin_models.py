from sqlalchemy import Column, Integer, String, Boolean
from app.models import Base


class Admin(Base):
    __tablename__ = 'admins'
    admin_id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
