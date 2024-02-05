# demo-django-seed-db

Example repo to demonstrate seed databases with Django.

## Quick start (given that you have poetry and docker-compose installed)

``` bash
# Create new virtual environment
poetry env

# Install dependencies
poetry run poetry install

# Bring up database
docker-compose up -d

# Run migrations
poetry run ./app/migrate.py migrate
```
