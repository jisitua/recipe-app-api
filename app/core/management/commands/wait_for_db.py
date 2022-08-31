"""
This forces app services to wait for the database to be \n
available before trying to start. This purpose of this to \n
prevent the app services from failing.
"""

import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Class for all managment commands for wait for db program"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database is unavailable.\
                    .. Retrying in 1 second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is ready!'))
