from sqlalchemy import text
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///myapp/test.db", echo=True, future=True)
conn = engine.connect()
conn.execute(text("DROP TABLE IF EXISTS user"))
conn.execute(text("CREATE TABLE user (name text)"))