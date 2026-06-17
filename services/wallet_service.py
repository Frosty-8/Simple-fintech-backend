<<<<<<< HEAD
# ------------------------------------------
# Imports
# ------------------------------------------
from fastapi import HTTPException
=======
from database.db import get_connection
from fastapi import HTTPException
from utils.generators import (
    generate_transaction_id
)
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98

from database.db import get_connection
from utils.generators import (
    generate_transaction_id
)


# ------------------------------------------
# Create Wallet
# ------------------------------------------
def create_wallet(
        wallet_id: str,
        user_id: str
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO wallets
        (
            wallet_id,
            user_id,
            balance
        )
        VALUES (?, ?, ?)
        """,
        (
            wallet_id,
            user_id,
            0
        )
    )

    conn.commit()
    conn.close()


# ------------------------------------------
# Get Wallet
# ------------------------------------------
def get_wallet(
        user_id: str
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM wallets
        WHERE user_id = ?
        """,
        (user_id,)
    )

    wallet = cursor.fetchone()

    conn.close()

    return wallet

<<<<<<< HEAD

# ------------------------------------------
# Deposit
# ------------------------------------------
def deposit(
        user_id: str,
        amount: float
=======
#--------------------------------
#        DEPOSIT
#--------------------------------
def deposit(
    user_id: str,
    amount: float
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
):
    conn = get_connection()
    cursor = conn.cursor()

<<<<<<< HEAD
    try:
        conn.execute("BEGIN")

        cursor.execute(
            """
            SELECT *
            FROM wallets
            WHERE user_id = ?
            """,
            (user_id,)
        )

        wallet = cursor.fetchone()

        if not wallet:
            raise HTTPException(
                status_code=404,
                detail="Wallet not found"
            )

=======
    try: 
        conn.execute("BEGIN")
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        cursor.execute(
            """
            UPDATE wallets
            SET balance = balance + ?
            WHERE user_id = ?
            """,
            (
                amount,
<<<<<<< HEAD
                user_id
            )
        )

=======
                user_id,
            )
        )

        cursor.execute(
            """
            SELECT wallet_id
            FROM wallets
            WHERE user_id = ?
            """,
            (user_id,)
        )

        wallet = cursor.fetchone()

>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        txn_id = generate_transaction_id()

        cursor.execute(
            """
<<<<<<< HEAD
            INSERT INTO transactions
            (
                transaction_id,
                sender_wallet,
                receiver_wallet,
                amount,
                transaction_type,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
=======
            INSERT INTO transactions 
            VALUES (
                ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP
            )
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
            """,
            (
                txn_id,
                None,
                wallet["wallet_id"],
                amount,
                "DEPOSIT",
                "SUCCESS"
            )
        )

        conn.commit()

<<<<<<< HEAD
        return {
            "message":
            "Deposit successful",
            "transaction_id":
            txn_id
        }

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


# ------------------------------------------
# Withdraw
# ------------------------------------------
def withdraw(
        user_id: str,
        amount: float
=======
    except:
        conn.rollback()
        raise HTTPException(
            status_code=500,
            detail="Deposit failed"
        )
    finally: 
        conn.close()



#--------------------------------
#        WITHDRAW
#--------------------------------

def withdraw(
    user_id: str,
    amount: float
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        conn.execute("BEGIN")

        cursor.execute(
            """
            SELECT *
            FROM wallets
            WHERE user_id = ?
            """,
            (user_id,)
        )

        wallet = cursor.fetchone()

        if not wallet:
            raise HTTPException(
                status_code=404,
                detail="Wallet not found"
            )

        if wallet["balance"] < amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient balance"
            )

        cursor.execute(
            """
            UPDATE wallets
            SET balance = balance - ?
            WHERE user_id = ?
            """,
            (
                amount,
                user_id
            )
        )

        txn_id = generate_transaction_id()

        cursor.execute(
            """
            INSERT INTO transactions
<<<<<<< HEAD
            (
                transaction_id,
                sender_wallet,
                receiver_wallet,
                amount,
                transaction_type,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
=======
            VALUES (
                ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP
            )
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
            """,
            (
                txn_id,
                wallet["wallet_id"],
                None,
                amount,
                "WITHDRAW",
                "SUCCESS"
            )
        )

        conn.commit()

<<<<<<< HEAD
        return {
            "message":
            "Withdrawal successful",
            "transaction_id":
            txn_id
        }

    except Exception:
=======
    except:
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        conn.rollback()
        raise

    finally:
        conn.close()

<<<<<<< HEAD

# ------------------------------------------
# Transfer
# ------------------------------------------
def transfer(
        sender_user_id: str,
        receiver_wallet_id: str,
        amount: float
=======
#--------------------------------
#        TRANSFER
#--------------------------------
def transfer(
    sender_user_id: str,
    receiver_wallet_id: str,
    amount: float
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        conn.execute("BEGIN")

<<<<<<< HEAD
        #
        # Sender wallet
        #
=======
        #---------------------------
        # Get sender wallet
        #---------------------------
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        cursor.execute(
            """
            SELECT *
            FROM wallets
            WHERE user_id = ?
            """,
            (sender_user_id,)
        )

        sender_wallet = cursor.fetchone()

        if not sender_wallet:
            raise HTTPException(
                status_code=404,
                detail="Sender wallet not found"
            )

<<<<<<< HEAD
        #
        # Receiver wallet
        #
=======
        #---------------------------
        # Get receiver wallet
        #---------------------------
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        cursor.execute(
            """
            SELECT *
            FROM wallets
            WHERE wallet_id = ?
            """,
            (receiver_wallet_id,)
        )

        receiver_wallet = cursor.fetchone()

        if not receiver_wallet:
            raise HTTPException(
                status_code=404,
                detail="Receiver wallet not found"
            )

<<<<<<< HEAD
        #
        # Prevent self transfer
        #
=======
        #---------------------------
        # Prevent self transfer
        #---------------------------
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        if (
            sender_wallet["wallet_id"]
            == receiver_wallet_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Cannot transfer to yourself"
            )

<<<<<<< HEAD
        #
        # Balance check
        #
=======
        #---------------------------
        # Balance check
        #---------------------------
        
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        if sender_wallet["balance"] < amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient balance"
            )

<<<<<<< HEAD
        #
        # Deduct sender
        #
=======
        #---------------------------
        # Deduct sender
        #---------------------------
        
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        cursor.execute(
            """
            UPDATE wallets
            SET balance = balance - ?
            WHERE wallet_id = ?
            """,
            (
                amount,
                sender_wallet["wallet_id"]
            )
        )

<<<<<<< HEAD
        #
        # Credit receiver
        #
=======
        #---------------------------
        # Credit receiver
        #---------------------------
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        cursor.execute(
            """
            UPDATE wallets
            SET balance = balance + ?
            WHERE wallet_id = ?
            """,
            (
                amount,
                receiver_wallet_id
            )
        )

<<<<<<< HEAD
        #
        # Create transaction
        #
=======
        #---------------------------
        # Create transaction
        #---------------------------
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        txn_id = generate_transaction_id()

        cursor.execute(
            """
            INSERT INTO transactions
<<<<<<< HEAD
            (
                transaction_id,
                sender_wallet,
                receiver_wallet,
                amount,
                transaction_type,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
=======
            VALUES (
                ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP
            )
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
            """,
            (
                txn_id,
                sender_wallet["wallet_id"],
                receiver_wallet_id,
                amount,
                "TRANSFER",
                "SUCCESS"
            )
        )

        conn.commit()

        return {
<<<<<<< HEAD
            "message":
            "Transfer successful",
            "transaction_id":
            txn_id,
            "sender_wallet":
            sender_wallet["wallet_id"],
            "receiver_wallet":
            receiver_wallet_id,
            "amount":
            amount
        }

    except Exception:
=======
            "transaction_id": txn_id,
            "amount": amount,
            "sender":
                sender_wallet["wallet_id"],
            "receiver":
                receiver_wallet_id
        }

    except:
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
        conn.rollback()
        raise

    finally:
        conn.close()