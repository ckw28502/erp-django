#!/bin/bash

set -e

python -m manage migrate

if [ "$1" = "prod" ]; then
    python -m manage runserver 0.0.0.0:8000
else
    python -m manage runserver
fi