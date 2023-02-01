"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with en email is successful."""
        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email, 'sample_password'
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating a user without an email raises a ValueError"""
        sample_email = ""

        self.assertRaises(
            ValueError,
            get_user_model().objects.create_user,
            sample_email, "sample_password"
        )

    def test_create_superuser_successful(self):
        """Test creating a superuser is successful."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            "sample_password"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
