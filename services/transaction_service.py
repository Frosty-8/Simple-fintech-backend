#
#
#
from database.db import get_connection

#--------------------------
#       Methods
#--------------------------

def get_transactions(
    wallet_id: str
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
    ]