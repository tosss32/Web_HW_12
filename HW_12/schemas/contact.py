from datetime import datetime
from pydantic import BaseModel

class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: datetime
    additional_data: str = None
    class Config:
        from_attributes = True


class ContactCreate(BaseModel):
    first_name: str
    last_name: str | None
    email: str | None
    phone_number: str
    birthday: datetime | None
    additional_data: str | None


class ContactUpdate(BaseModel):
    first_name: str | None
    last_name: str | None
    email: str | None
    phone_number: str | None
    birthday: datetime | None
    additional_data: str | None