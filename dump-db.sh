#!/usr/bin/bash

docker-compose exec -e PGPASSWD=postgres postgres pg_dump -U postgres > seed-db.sql
