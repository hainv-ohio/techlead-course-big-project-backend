# Order service

## Init db

Run SQL to create user and database for this service

```bash
psql postgres://postgres:12345@localhost:5432/postgres << SQL
CREATE DATABASE order_db;
CREATE USER order_service WITH ENCRYPTED PASSWORD 'User12345';
GRANT ALL PRIVILEGES ON DATABASE order_db TO order_service;
SQL
```