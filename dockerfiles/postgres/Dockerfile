FROM postgres:13-alpine
ENV POSTGRES_PASSWORD=postgres
COPY init.sql /docker-entrypoint-initdb.d/

# docker build -f dockerfiles/postgres/Dockerfile -t rates_dj2_postgres .
# docker run -p 5433:5432 -v ratesdj2_rates_dj2_postgres:/var/lib/postgresql/data
# psql -U rates_dj2_app -h localhost -p 5433 rates_dj2_app
