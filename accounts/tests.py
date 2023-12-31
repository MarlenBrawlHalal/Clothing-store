from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='biba', email='biba@email.com', password='123dias123'
        )
        self.assertEqual(user.username, 'biba')
        self.assertEqual(user.email, 'biba@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username='superbiba', email='superbiba@email.com', password='123dias123'
        )
        self.assertEqual(superuser.username, 'superbiba')
        self.assertEqual(superuser.email, 'superbiba@email.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 'I should not be here')

    def test_signup_form(self):
        user = get_user_model()
        new_user = user.objects.create_user(username='biba', email='biba@email.com') # Not necessary to add all fields
        self.assertEqual(user.objects.all().count(), 1)
        self.assertEqual(user.objects.all()[0].username, 'biba')
        self.assertEqual(user.objects.all()[0].email, 'biba@email.com')