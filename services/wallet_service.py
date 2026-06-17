# ------------------------------------------
# Imports
# ------------------------------------------
from fastapi import HTTPException

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


# ------------------------------------------
# Deposit
# ------------------------------------------
def deposit(
        user_id: str,
        amount: float
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

        cursor.execute(
            """
            UPDATE wallets
            SET balance = balance + ?
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
            (
                transaction_id,
                sender_wallet,
                receiver_wallet,
                amount,
                transaction_type,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
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
            (
                transaction_id,
                sender_wallet,
                receiver_wallet,
                amount,
                transaction_type,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
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

        return {
            "message":
            "Withdrawal successful",
            "transaction_id":
            txn_id
        }

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


# ------------------------------------------
# Transfer
# ------------------------------------------
def transfer(
        sender_user_id: str,
        receiver_wallet_id: str,
        amount: float
):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        conn.execute("BEGIN")

        #
        # Sender wallet
        #
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

        #
        # Receiver wallet
        #
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

        #
        # Prevent self transfer
        #
        if (
            sender_wallet["wallet_id"]
            == receiver_wallet_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Cannot transfer to yourself"
            )

        #
        # Balance check
        #
        if sender_wallet["balance"] < amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient balance"
            )

        #
        # Deduct sender
        #
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

        #
        # Credit receiver
        #
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

        #
        # Create transaction
        #
        txn_id = generate_transaction_id()

        cursor.execute(
            """
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
        conn.rollback()
        raise

    finally:
        conn.close()