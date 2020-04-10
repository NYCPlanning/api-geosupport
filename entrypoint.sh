#!/bin/bash
if [ -z "$PORT" ]
then export PORT=5000
else
    echo "port is $PORT"
fi
gunicorn app:app --bind=:$PORT --workers=5 --threads=3
