#!/bin/bash
sleep 5
alembic upgrade head
uvicorn "app.main:app" --host 0.0.0.0 --port=${PORT:-5000}