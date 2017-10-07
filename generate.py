import os
from hashlib import md5

from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('/usr/local/docker'))
template = env.get_template('traefik.toml.j2')

TRAEFIK_DEV = os.environ.get('TRAEFIK_DEV', False)
TRAEFIK_DOMAIN = os.environ.get('TRAEFIK_DOMAIN', 'localhost')
TRAEFIK_ACME_EMAIL = os.environ.get('TRAEFIK_ACME_EMAIL')
TRAEFIK_WEB_PASSWORD = os.environ.get('TRAEFIK_WEB_PASSWORD', 'admin')
TRAEFIK_WEB_USER = os.environ.get('TRAEFIK_WEB_USER', 'admin')

pwhash = md5('{}:traefik:{}'.format(TRAEFIK_WEB_USER, TRAEFIK_WEB_PASSWORD)).hexdigest()
web_users = ['{}:traefik:{}'.format(TRAEFIK_WEB_USER, pwhash)]


context = {
    'TRAEFIK_DEV': TRAEFIK_DEV,
    'TRAEFIK_DOMAIN': TRAEFIK_DOMAIN,
    'TRAEFIK_ACME_EMAIL': TRAEFIK_ACME_EMAIL,
    'web_users': web_users,
}

output_from_parsed_template = template.render(**context)

with open("/usr/local/traefik/traefik.toml", "wb") as fh:
    fh.write(output_from_parsed_template)
