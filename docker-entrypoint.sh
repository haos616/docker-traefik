#!/bin/sh

touch /usr/local/traefik/acme.json || exit 1

chmod 600 /usr/local/traefik/acme.json || exit 1

python /usr/local/docker/generate.py || exit 1

/entrypoint.sh "$@"
