from fastapi import (
    HTTPException, Depends
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from services.user_service import (
    get_user_by_email
)

from utils.hashing import (
    verify_password
)

from utils.jwt_handler import (
    create_access_token, verify_token
)

security = HTTPBearer()

def login_user(
        email: str,
        password: str
):
    user = get_user_by_email(email)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    
    valid = verify_password(
        password,
        user["password"]
    )

    if not valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    
    token = create_access_token({
        "sub": user["id"],
        "email": user["email"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    try:
        payload = verify_token(token)

        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )