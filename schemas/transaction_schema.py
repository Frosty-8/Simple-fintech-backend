from pydantic import BaseModel

class TransactionResponse(BaseModel):
    transaction_id: str
    sender_wallet: str | None
    receiver_wallet: str | None
    amount: float
    transaction_type: str
    status: str
    created_at: str