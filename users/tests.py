from django.test import TestCase
from django.urls import reverse

from blog.factories import UserFactory
from .models import User
from users.forms import UserRegForm


class UserTest(TestCase):
    """Tests for User model."""

    def test_add_user(self):

        self.user = UserFactory()
        user = User.objects.get(id=self.user.id)

        self.assertEqual(user.first_name, self.user.first_name)


class RegistrationViewTests(TestCase):
    """Tests for Registration view."""

    def test_get_reg_form(self):
        self.url = reverse('reg')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_post_reg_form(self):
        self.url = reverse('reg')

        response = self.client.post(self.url, {'username': '', 'email': '', 'password1': ''})
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'password1', 'This field is required.')

        response = self.client.post(self.url, {
            'username': 'Alex',
            'email': 'email@gmail.com',
            'password1': 'qwerty212',
            'password2': 'qwerty212',
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('log'))

    def test_valid_forms(self):
        valid_data = {
            'username': 'Alex',
            'email': 'email@gmail.com',
            'password1': 'qwerty212',
            'password2': 'qwerty212',
        }
        form = UserRegForm(data=valid_data)

        self.assertTrue(form.is_valid())

    def test__not_valid_forms(self):
        not_valid_data = {
            'username': 'Alex',
            'email': 'email@gmail.com',
        }
        form = UserRegForm(data=not_valid_data)

        self.assertFalse(form.is_valid())
