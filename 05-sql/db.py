import os
import sqlite3

def execute_query(query, args=()):
    conn = sqlite3.connect(
        os.path.join(
            os.path.dirname(__file__),
            'chinook.db'
        )
    )
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    result = cur.fetchall()
    conn.commit()
    return result
