ARG TRAEFIK_VERSION=

FROM traefik:${TRAEFIK_VERSION}-alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install Jinja2 \
  && rm -rf /var/cache/apk/*

ADD traefik.toml.j2 docker-entrypoint.sh generate.py /usr/local/docker/

RUN mkdir /usr/local/traefik \
    && chmod +x /usr/local/docker/docker-entrypoint.sh

WORKDIR /usr/local/traefik

VOLUME /usr/local/traefik

ENTRYPOINT ["/usr/local/docker/docker-entrypoint.sh"]

CMD ["traefik"]
