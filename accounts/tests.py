from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='nobody', email='nobody@user.com', password='foo')
        self.assertEqual(user.username, 'nobody')
        self.assertEqual(user.email, 'nobody@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('administration', 'admin@user.com', 'foo')
        self.assertEqual(admin_user.username, 'administration')
        self.assertEqual(admin_user.email, 'admin@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='administration', email='admin@user.com', password='foo', is_superuser=False)
