#!/bin/bash

set -e

python -m manage migrate
python -m manage runserver