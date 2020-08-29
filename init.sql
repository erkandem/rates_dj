-- every user should have it's own database, which has the same name as the user
CREATE DATABASE rates_dj2_app;
CREATE ROLE rates_dj2_app WITH PASSWORD 'postgres';

-- set some default which will prevent lookup queries and therefore speed up all queries
-- source https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
ALTER ROLE rates_dj2_app SET client_encoding TO 'utf8';
ALTER ROLE rates_dj2_app SET default_transaction_isolation TO 'read committed';
ALTER ROLE rates_dj2_app SET timezone TO 'UTC';
ALTER ROLE rates_dj2_app WITH LOGIN;
ALTER ROLE rates_dj2_app WITH SUPERUSER;

-- grant rights to read, write, ... and so on
GRANT ALL PRIVILEGES ON DATABASE rates_dj2_app TO rates_dj2_app;
