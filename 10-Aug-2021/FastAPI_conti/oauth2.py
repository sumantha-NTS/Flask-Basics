from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
import token_1


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token_1.Verify_token(token, credentials_exception)
