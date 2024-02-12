from sqlalchemy import  Column, String, DateTime
from .base import BaseModel, Base

class ContactDB(BaseModel):
    __tablename__ = "contacts"
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    birthday = Column(DateTime)
    additional_data = Column(String, nullable=True)