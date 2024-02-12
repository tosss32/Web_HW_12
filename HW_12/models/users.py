from sqlalchemy import  Column, String, DateTime
from .base import BaseModel

class UsertDB(BaseModel):
    __tablename__ = "users"
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)
    