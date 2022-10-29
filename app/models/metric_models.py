from sqlalchemy import Column, Integer, Date, String
from sqlalchemy.sql import func
from app.models import Base


class Registration(Base):
    __tablename__ = 'registrations'
    reg_id = Column(Integer, autoincrement=True, primary_key=True)
    method = Column(String(50), nullable=False)
    date_registered = Column(Date, server_default=func.current_date())
