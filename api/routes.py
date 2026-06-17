# ------------------------------------------
# Imports
# ------------------------------------------
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

# Schemas
from schemas.user_schema import (
    UserRegister,
    UserLogin
)

from schemas.wallet_schema import (
    DepositRequest,
    WithdrawRequest,
    TransferRequest
)

# Services
from services.user_service import (
    create_user
)

from services.wallet_service import (
    create_wallet,
<<<<<<< HEAD
    get_wallet,
    deposit,
    withdraw,
=======
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
    transfer
)

from services.transaction_service import (
    get_transactions
)

# Authentication
from users.auth import (
    login_user,
    get_current_user
)

<<<<<<< HEAD
=======
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
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98

# ------------------------------------------
# Router
# ------------------------------------------
router = APIRouter()


# ------------------------------------------
# Home
# ------------------------------------------
@router.get("/")
def home():
    return {
        "message": "Fintech Wallet API Running"
    }

<<<<<<< HEAD

# ------------------------------------------
# Register
# ------------------------------------------
=======
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
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


# ------------------------------------------
# Login
# ------------------------------------------
@router.post("/login")
def login(
    payload: UserLogin
):
    return login_user(
        payload.email,
        payload.password
    )


# ------------------------------------------
# Profile
# ------------------------------------------
@router.get("/profile")
def profile(
    user=Depends(get_current_user)
):
    return user


# ------------------------------------------
# Wallet
# ------------------------------------------
@router.get("/wallet")
def wallet(
    user=Depends(get_current_user)
):
    wallet = get_wallet(
        user["sub"]
    )

    if not wallet:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )
<<<<<<< HEAD

    return dict(wallet)


# ------------------------------------------
# Deposit
# ------------------------------------------
=======
    
    return dict(wallet)

>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
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
<<<<<<< HEAD
        "message": "Money deposited successfully"
    }


# ------------------------------------------
# Withdraw
# ------------------------------------------
=======
        "message":
        "Money deposited successfully"
    }

>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
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
<<<<<<< HEAD
        "message": "Money withdrawn successfully"
    }


# ------------------------------------------
# Transfer
# ------------------------------------------
=======
        "message":
        "Money withdrawn successfully"
    } 


>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
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


<<<<<<< HEAD
# ------------------------------------------
# Transactions
# ------------------------------------------
@router.get("/transactions")
=======
@router.post("/transactions")
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
def transactions(
    user=Depends(get_current_user)
):
    wallet = get_wallet(
        user["sub"]
    )

<<<<<<< HEAD
    if not wallet:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )

    return get_transactions(
        wallet["wallet_id"]
    )


# ------------------------------------------
# Debug Routes
# ------------------------------------------
print("\nROUTER ROUTES:")
for route in router.routes:
    methods = ", ".join(route.methods)
    print(f"{methods:15} {route.path}")
=======
    return get_transactions(
        wallet["wallet_id"]
    )
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
