"""
Tests for models.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Test class for models"""

    def test_create_user_with_email(self):
        """Test creating a user with an email"""
        email = 'email@example.com'
        password = 'test@pass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
