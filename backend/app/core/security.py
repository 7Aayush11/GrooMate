from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRETT_KEY = "somesecretyoudontknow"
ALGORITHM = "HS256"

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(datetime.timezone.utc) + timedelta(hours =2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRETT_KEY, algorithm=ALGORITHM)
