from users.models import User
from django.db import IntegrityError
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)
FIELDS = ['first_name', 'last_name', 'birthday', 'registration']


def parse(self, request, file):
    lines = file.read().splitlines()
    for line in lines[1:]:
        pairs = dict(zip(FIELDS, line.decode('utf-8').split(',')))
        change_format(pairs)
        user = User(**pairs)
        save(self, request, user)


def save(self, request, user):
    try:
        user.save()
    except IntegrityError as e:
        logger.error(e)
        self.message_user(
            request,
            "Error occurred while saving into the database."
        )
    except ValidationError as e:
        logger.error(e)
        self.message_user(
            request,
            "Incorrect data : {}".format(
                e.message
            )
        )


def change_format(pairs):
    pairs['birthday'] = pairs['birthday'].replace('/', '-')
    pairs['registration'] = pairs['registration'].replace('/', '-')
