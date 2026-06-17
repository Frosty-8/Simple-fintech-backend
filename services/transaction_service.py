<<<<<<< HEAD
# ------------------------------------------
# Imports
# ------------------------------------------
from database.db import get_connection


# ------------------------------------------
# Get All Transactions For Wallet
# ------------------------------------------
def get_transactions(
        wallet_id: str
=======
#
#
#
from database.db import get_connection

#--------------------------
#       Methods
#--------------------------

def get_transactions(
    wallet_id: str
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM transactions
        WHERE sender_wallet = ?
           OR receiver_wallet = ?
        ORDER BY created_at DESC
        """,
        (
            wallet_id,
            wallet_id
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        dict(row)
        for row in rows
<<<<<<< HEAD
    ]


# ------------------------------------------
# Get Single Transaction
# ------------------------------------------
def get_transaction_by_id(
        transaction_id: str
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM transactions
        WHERE transaction_id = ?
        """,
        (transaction_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if not row:
        return None

    return dict(row)


# ------------------------------------------
# Get Recent Transactions
# ------------------------------------------
def get_recent_transactions(
        wallet_id: str,
        limit: int = 5
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM transactions
        WHERE sender_wallet = ?
           OR receiver_wallet = ?
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (
            wallet_id,
            wallet_id,
            limit
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        dict(row)
        for row in rows
    ]


# ------------------------------------------
# Get Transaction Statistics
# ------------------------------------------
def get_transaction_stats(
        wallet_id: str
):
    conn = get_connection()
    cursor = conn.cursor()

    #
    # Total Transactions
    #
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM transactions
        WHERE sender_wallet = ?
           OR receiver_wallet = ?
        """,
        (
            wallet_id,
            wallet_id
        )
    )

    total_transactions = cursor.fetchone()[0]

    #
    # Total Money Sent
    #
    cursor.execute(
        """
        SELECT
            COALESCE(
                SUM(amount),
                0
            )
        FROM transactions
        WHERE sender_wallet = ?
        """,
        (wallet_id,)
    )

    total_sent = cursor.fetchone()[0]

    #
    # Total Money Received
    #
    cursor.execute(
        """
        SELECT
            COALESCE(
                SUM(amount),
                0
            )
        FROM transactions
        WHERE receiver_wallet = ?
        """,
        (wallet_id,)
    )

    total_received = cursor.fetchone()[0]

    conn.close()

    return {
        "total_transactions":
            total_transactions,
        "total_sent":
            total_sent,
        "total_received":
            total_received
    }
=======
    ]
>>>>>>> 2448d9e1b8758c90d3a2e8f15811144694734f98
