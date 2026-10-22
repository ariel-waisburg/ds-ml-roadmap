"""Chequea que las librerías principales importen y que el Postgres local responda."""

import importlib

LIBS = [
    "numpy",
    "pandas",
    "scipy",
    "statsmodels",
    "sklearn",
    "xgboost",
    "lightgbm",
    "matplotlib",
    "seaborn",
    "duckdb",
    "nltk",
]


def check_libs() -> bool:
    ok = True
    for name in LIBS:
        try:
            module = importlib.import_module(name)
            print(f"  ok  {name} {getattr(module, '__version__', '')}")
        except ImportError as error:
            ok = False
            print(f"  ERROR  {name}: {error}")
    return ok


def check_db() -> bool:
    from sqlalchemy import text

    from roadmap_utils.db import get_engine

    try:
        with get_engine().connect() as conn:
            version = conn.execute(text("select version()")).scalar_one()
        print(f"  ok  {version.split(',')[0]}")
        return True
    except Exception as error:  # noqa: BLE001 - queremos mostrar cualquier falla de conexión
        print(f"  ERROR  no conecta a Postgres ({type(error).__name__}). ¿Corriste `make db-up`?")
        return False


if __name__ == "__main__":
    print("Librerías:")
    libs_ok = check_libs()
    print("Base de datos:")
    db_ok = check_db()
    print("\nTodo listo." if libs_ok and db_ok else "\nHay cosas para revisar arriba.")
