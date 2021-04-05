from sqlalchemy import text
from myapp import conn

def insert_user(name):
    conn.execute(text("INSERT INTO USER(name) VALUES(:name)"), 
        [{"name": "ahlev"}])
    conn.commit()

def find_user(name):
    results = conn.execute(text("SELECT name FROM user WHERE name = :name"), 
        [{"name": "ahlev"}])
    return results.fetchall()
