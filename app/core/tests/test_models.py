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


    def test_new_user_email_normalized(self):
        """Test email is normailzed for new users."""
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@ExaMplE.cOm', 'Test2@example.com'],
        ]
        for email, output_result in sample_emails:
            user = get_user_model().objects.create_user(email, 'pas234')
            self.assertEqual(user.email, output_result)


    def test_user_without_email_exception(self):
        """Deprieve users from creating users without an email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')


    def test_user_is_superuser(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'test_superuser@example.com',
            'Password123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
