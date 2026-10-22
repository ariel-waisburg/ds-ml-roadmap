# sql/

Ejercicios de SQL contra el Postgres local (`make db-up`). Un archivo por tanda: `semana-01-diagnostico.sql`, `semana-03-cohortes.sql`, etc.

Para correrlos: `docker exec -i ds-postgres psql -U ds -d ds < sql/archivo.sql`, o desde un notebook con `roadmap_utils.db.get_engine()` y `pandas.read_sql`.

Práctica diaria: StrataScratch o LeetCode. Acá quedan los que vale la pena guardar, con un comentario de qué enseñan.
