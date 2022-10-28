from sqlalchemy import Column, Integer, Date, String
from sqlalchemy.sql import func
from app.models import Base
from abc import ABC, abstractmethod


class Counter(ABC):

    @abstractmethod
    def count():
        pass


class Registration(Base):
    __tablename__ = 'registrations'
    reg_id = Column(Integer, autoincrement=True, primary_key=True)
    method = Column(String(50), nullable=False)
    date_registered = Column(Date, server_default=func.current_date())


class FederatedIdRegistrationCounter(Counter):
    def count(session, date_from):
        print(date_from)
        return session.query(Registration).filter_by(method='federatedidentity').count()


class MailPasswordRegistrationCounter(Counter):
    def count(session, date_from):
        print(date_from)
        return session.query(Registration).filter_by(method='mailpassword').count()
