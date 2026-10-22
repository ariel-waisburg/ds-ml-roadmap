# ds-ml-roadmap

Mi vuelta al mundo de la data: 11 semanas (oct 2026 – ene 2027) para reactivar estadística y machine learning, construir dos proyectos end-to-end y llegar a febrero listo para trabajar como **Data Scientist / ML Engineer**.

Este repo es el cuaderno de trabajo: un notebook (o más) por semana, ejercicios de SQL y notas de lo que voy aprendiendo. Los dos proyectos de portfolio viven en repos propios.

## Plan

| Fase | Semanas | Foco |
| --- | --- | --- |
| 1 · Reactivar | 1–6 (26 oct – 6 dic) | Estadística, ML supervisado y no supervisado, series de tiempo, LLMs |
| 2 · Construir | 7–11 (7 dic – 10 ene) | Proyecto 1 (modelo en producción) y Proyecto 2 (asistente de jurisprudencia con LLMs) |
| 3 · Buscar | desde el 1 dic | Aplicaciones, entrevistas, take-homes |

El detalle semana a semana está en [`semanas/`](semanas/README.md).

## Estructura

```
.
├── semanas/            # una carpeta por semana: notebooks + README con objetivo y entregable
├── sql/                # ejercicios de SQL contra el Postgres local
├── notas/              # huecos detectados, dudas, cosas para repasar
├── src/roadmap_utils/  # helpers que reutilizo entre notebooks (rutas, conexión a la base)
├── scripts/            # utilidades de línea de comando (chequeo del entorno)
├── tests/              # tests de los helpers
├── data/               # datasets locales (fuera de git)
└── docker-compose.yml  # Postgres 16 para practicar SQL
```

## Cómo arrancar

Requisitos: [uv](https://docs.astral.sh/uv/), Docker y git.

```bash
make setup     # instala dependencias, hooks de pre-commit y crea .env
make db-up     # levanta Postgres en localhost:5432
make check     # verifica librerías y conexión a la base
make lab       # abre JupyterLab
```

Sin `make`: `uv sync`, `uv run pre-commit install`, `cp .env.example .env`, `docker compose up -d`, `uv run python scripts/check_env.py`, `uv run jupyter lab`.

Para sumar librerías a medida que avanza el plan (por ejemplo en la semana 6): `uv add <paquete>`.

## Cómo trabajo

- **Una rama y un PR por semana** (`semana-01`, `semana-02`, …). El PR se mergea cuando el entregable está listo y el CI está en verde.
- **CI en GitHub Actions**: lint y formato con ruff, tests con pytest, en cada push y PR.
- **Notebooks sin outputs en git**: nbstripout los limpia en el pre-commit, así los diffs se leen.
- **Datos fuera de git**: todo lo que va en `data/` se ignora; cada notebook dice de dónde bajar su dataset.
- **Credenciales en `.env`** (copiar de `.env.example`), nunca en el código.

## Progreso

| Semana | Tema | Estado |
| --- | --- | --- |
| 1 | Arranque y diagnóstico | En curso |
| 2 | Inferencia y visualización | Pendiente |
| 3 | Regresión y causalidad | Pendiente |
| 4 | ML supervisado | Pendiente |
| 5 | No supervisado y series de tiempo | Pendiente |
| 6 | Texto y LLMs | Pendiente |
| 7–8 | Proyecto 1 | Pendiente |
| 9–11 | Proyecto 2 | Pendiente |

## Proyectos

- **Proyecto 1 · Modelo en producción**: XGBoost, MLflow, DVC, FastAPI, Docker, GitHub Actions, AWS. _Repo: pronto._
- **Proyecto 2 · Asistente de jurisprudencia argentina**: clasificación LLM vs. clásico, RAG con citas, agente con LangGraph, guardrails y monitoreo. _Repo: pronto._
