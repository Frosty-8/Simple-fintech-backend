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
    create_wallet,
    transfer
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
    get_wallet,
    deposit,
    withdraw
)

from schemas.wallet_schema import (
    DepositRequest,
    WithdrawRequest,
    TransferRequest
)

from services.transaction_service import (
    get_transactions
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

@router.post("/register")
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

@router.post("/deposit")
def deposit_money(
    payload: DepositRequest,
    user=Depends(get_current_user)
):
    deposit(
        user["sub"],
        payload.amount
    )

    return {
        "message":
        "Money deposited successfully"
    }

@router.post("/withdraw")
def withdraw_money(
    payload: WithdrawRequest,
    user=Depends(get_current_user)
):
    withdraw(
        user["sub"],
        payload.amount
    )

    return {
        "message":
        "Money withdrawn successfully"
    } 


@router.post("/transfer")
def transfer_money(
    payload: TransferRequest,
    user=Depends(get_current_user)
):
    return transfer(
        user["sub"],
        payload.receiver_wallet_id,
        payload.amount
    )


@router.post("/transactions")
def transactions(
    user=Depends(get_current_user)
):
    wallet = get_wallet(
        user["sub"]
    )

    return get_transactions(
        wallet["wallet_id"]
    )