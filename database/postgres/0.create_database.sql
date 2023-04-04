CREATE DATABASE simple_search_engine_db WITH ENCODING = 'UTF8';
CREATE USER simple_search_engine_owner WITH PASSWORD 'Very!Strong1Password0';
GRANT ALL PRIVILEGES ON DATABASE simple_search_engine_db TO simple_search_engine_owner;