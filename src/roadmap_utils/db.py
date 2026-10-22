"""Conexión al Postgres local de docker-compose."""

import os

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine

from roadmap_utils.paths import REPO_ROOT

DEFAULT_URL = "postgresql+psycopg://ds:ds@localhost:5432/ds"


def get_engine() -> Engine:
    """Devuelve un engine de SQLAlchemy usando DATABASE_URL del .env."""
    load_dotenv(REPO_ROOT / ".env")
    return create_engine(os.getenv("DATABASE_URL", DEFAULT_URL))
