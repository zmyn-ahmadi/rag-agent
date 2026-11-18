from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg://zmn@localhost/agent_memory_db")
with engine.begin() as conn:
    conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))


def get_engine():
    return engine
