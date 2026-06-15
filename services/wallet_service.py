from database.db import get_connection

def create_wallet(
        wallet_id : str,
        user_id : str
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        
        INSERT INTO wallets 
                   (
                        wallet_id, 
                        user_id, 
                        balance
                   )
                   VALUES (?,?,?)
                   """,
                   (
                       wallet_id,
                       user_id,
                       0
                   )
                   
        )
    conn.commit()
    conn.close()



def get_wallet(user_id: str):
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