import sqlite3
import pytest

@pytest.mark.sql
def test_sqlite_insert_and_select(tmp_path):
    db = tmp_path / "test.db"
    conn = sqlite3.connect(db)
    try:
        cur = conn.cursor()
        cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")
        cur.execute("INSERT INTO users(name) VALUES (?)", ("Ner",))
        conn.commit()
        cur.execute("SELECT name FROM users WHERE id=1")
        assert cur.fetchone()[0] == "Ner"
    finally:
        conn.close()
