import datetime
import jwt
import hashlib

from fastapi import Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from services.users import UserService
from dependencies.database import get_db, SessionLocal

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from services.users import UserService

secret_key = "secret_key"


def create_access_token(username: str):
    token_data = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)  
    }
    token = jwt.encode(token_data, secret_key, algorithm="HS256")
    return token

def decode_jwt_token(token):
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Invalid token"


def verify_password(plain_password, hashed_password, salt):
    salted_password = (plain_password + salt).encode()
    hashed_input = hashlib.sha256(salted_password).hexdigest()
    return hashed_input == hashed_password


async def get_current_user(token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(get_db)):
    token = decode_jwt_token(token)
    user_service = UserService(db)
    username = token.get("sub")
    user = user_service.get_by_username(username)
    return user 
