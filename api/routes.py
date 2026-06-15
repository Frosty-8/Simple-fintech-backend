#------------------------------------------
#   Importing the Library
#------------------------------------------
from fastapi import APIRouter, HTTPException, Depends

from schemas.user_schema import (
    UserRegister
)

from services.user_service import (
    create_user
)

from services.wallet_service import (
    create_wallet
)

from schemas.user_schema import (
    UserLogin
)

from users.auth import (
    login_user
)

from users.auth import (
    get_current_user
)

from services.wallet_service import (
    get_wallet
)


#-----------------------------------
#   Router
#-----------------------------------
router = APIRouter()

@router.get("/")
def home():
    return {
        "message":"Fintech WALLET API Running"
    }

@router.post("/post")
def register(
    payload: UserRegister
):
    try:
        user = create_user(
            payload.name,
            payload.email,
            payload.password
        )
        create_wallet(
            user["wallet_id"],
            user["id"]
        )

        return {
            "message": "User registered successfully",
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "wallet_id": user["wallet_id"]
            }
        }
    
    except Exception as e: 
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@router.post("/login")
def login(
    payload: UserLogin
):
    return login_user(
        payload.email,
        payload.password
    )


@router.get("/profile")
def profile(
    user=Depends(
        get_current_user
    )
):
    return user

@router.get("/wallet")
def wallet(
    user = Depends(get_current_user)
):
    wallet = get_wallet(user["sub"])

    if not wallet:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )
    
    return dict(wallet)