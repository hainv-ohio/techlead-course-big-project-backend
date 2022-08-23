

## Init db

Run SQL to create user and database for this service

```bash
psql postgres://postgres:12345@localhost:5435/postgres << SQL
CREATE DATABASE user_db;
CREATE USER user_service WITH ENCRYPTED PASSWORD 'User12345';
GRANT ALL PRIVILEGES ON DATABASE user_db TO user_service;
SQL
```