"""Rutas del repo, para que los notebooks no dependan de desde dónde se abren."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"


def ensure_data_dirs() -> None:
    """Crea data/raw y data/processed si no existen."""
    for folder in (RAW_DIR, PROCESSED_DIR):
        folder.mkdir(parents=True, exist_ok=True)
