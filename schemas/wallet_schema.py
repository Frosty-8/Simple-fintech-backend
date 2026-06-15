from pydantic import (
    BaseModel, Field
)

class DepositRequest(BaseModel):
    amount: float = Field(gt=0)


class WithdrawRequest(BaseModel):
    amount: float = Field(gt=0)

class TransferRequest(BaseModel):
    receiver_wallet_id: str
    amount: float = Field(gt=0)


