from sqlalchemy import text

from app.core.db import Base, engine


def init_db() -> None:
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
    print("db initialized")
