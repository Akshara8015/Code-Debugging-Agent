import sqlite3

def init_db():
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS corrected_codes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        problem_id TEXT,
        problem_statement TEXT,
        code TEXT,
        error TEXT,
        analysis TEXT,
        iteration INTEGER
    )
    """)

    conn.commit()
    conn.close()

def insert_code(problem_id, code, problem_statement, error, analysis, iteration):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO corrected_codes (problem_id, code, problem_statement, error, analysis, iteration)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (problem_id, code, problem_statement, error, analysis, iteration))

    conn.commit()
    conn.close()

def get_recent_attempts(problem_id, limit=3):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT code, error, analysis FROM corrected_codes
    WHERE problem_id = ?
    ORDER BY id DESC
    LIMIT ?
    """, (problem_id, limit))

    rows = cursor.fetchall()
    conn.close()

    return [
        {"code": r[0], "error": r[1], "analysis": r[2]}
        for r in rows
    ]

def get_all_data():
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM corrected_codes""")

    for row in cursor.fetchall() :
        print(row)

    conn.commit()
    conn.close()

def delete_all_data():
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM corrected_codes""")

    for row in cursor.fetchall() :
        print(row)

    conn.commit()
    conn.close()

