"""
Unit tests for Django commands
"""
from django.test import SimpleTestCase
from django.core.management import call_command
from django.db.utils import OperationalError

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    '''Test commands class'''

    def test_wait_db_ready(self, check_result):
        """Test if waiting for db to confirm if the database is ready"""
        check_result.return_value = True

        call_command('wait_for_db')

        check_result.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, sleep_result, check_result):
        """Test wait for db command when getting OperationError"""
        check_result.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(check_result.call_count, 6)
        check_result.assert_called_with(databases=['default'])
