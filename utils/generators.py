import uuid

def generate_user_id():
    return f"USR-{uuid.uuid4().hex[:8]}"

def generate_wallet_id():
    return f"WAL-{uuid.uuid4().hex[:8]}"

def generate_transaction_id():
    return f"TXN-{uuid.uuid4().hex[:8]}"