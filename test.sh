#!/bin/bash
set -e

[ -f .env ] || touch .env

docker-compose run --rm hapy sh -c "cd /hapy/src && python -m unittest discover -s hapy/tests/"
