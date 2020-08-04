from users.models import User
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)
FIELDS = ['first_name', 'last_name', 'birthday', 'registration']


def parse(file):
    lines = file.read().splitlines()
    for line in lines[1:]:
        pairs = dict(zip(FIELDS, line.decode('utf-8').split(',')))
        change_format(pairs)
        user = User(**pairs)
        save(user)


def save(user):
    try:
        user.save()
    except IntegrityError as e:
        logger.error(e)


def change_format(pairs):
    pairs['birthday'] = pairs['birthday'].replace('/', '-')
    pairs['registration'] = pairs['registration'].replace('/', '-')
