from django.test import TestCase
from core.views import get_index
from contact.views import contact
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from accounts.models import User
from accounts.forms import UserRegistrationForm
from django import forms


class HomePageTest(TestCase):
    fixtures = ['subjects']

    def test_home_page_resolves(self):
        home_page = resolve('/')

        self.assertEqual(home_page.func, get_index)

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')

        self.assertTemplateUsed(home_page, "index.html")

        home_page_template_output = render_to_response("index.html").content

        self.assertEquals(home_page.content, home_page_template_output)


class ContactPageTest(TestCase):
    def test_contact_page_resolves(self):
        contact_page = resolve('/contact/')

        self.assertEqual(contact_page.func, contact)


class CustomUserTest(TestCase):
    def test_manager_create(self):
        user = User.objects._create_user(None, "test@test.com", "password", False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password", False, False)

    def test_registration_form(self):
        form = UserRegistrationForm({
            'password1': 'letmein',
            'password2': 'letmein'
        })

        self.assertTrue(form.is_valid())
        self.assertRaisesMessage(form.ValidationError, "This field is required.", form.clean)
