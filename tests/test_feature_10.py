from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .utils import Document


class FeatureTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get("/accounts/signup/")
        self.content = self.response.content.decode("utf-8")
        self.document = Document()
        self.document.feed(self.content)

    def test_signup_resolves_to_accounts_signup(self):
        path = reverse("signup")
        self.assertEqual(
            path,
            "/accounts/signup/",
            msg="Could not resolve path name 'signup' to '/accounts/signup/",
        )

    def test_accounts_signup_returns_200(self):
        self.assertEqual(
            self.response.status_code,
            200,
            msg="Did not get the signup page",
        )

    def test_page_has_fundamental_five(self):
        self.assertTrue(
            self.document.has_fundamental_five(),
            msg="The response did not have the fundamental five",
        )

    def test_form_is_post(self):
        form = self.document.select("html", "body", "main", "div", "form")
        self.assertIsNotNone(
            form,
            msg=(
                "Did not find the form at the path "
                "html > body > main > div > form"
            ),
        )
        self.assertIn(
            "method",
            form.attrs,
            msg="Did not find 'method' for the form",
        )
        self.assertEqual(
            form.attrs.get("method").lower(),
            "post",
            msg="Form was not a post form",
        )

    def test_form_has_username_input(self):
        form = self.document.select("html", "body", "main", "div", "form")
        inputs = form.get_all_children("input")
        username = None
        for input in inputs:
            if input.attrs.get("name") == "username":
                username = input
                break
        self.assertIsNotNone(
            username,
            msg="Could not find the username input",
        )

    def test_form_has_password_input(self):
        form = self.document.select("html", "body", "main", "div", "form")
        inputs = form.get_all_children("input")
        password = None
        for input in inputs:
            if input.attrs.get("name") == "password":
                password = input
                break
        self.assertIsNotNone(
            password,
            msg="Could not find the password1 input",
        )

    def test_form_has_password_confirmation_input(self):
        form = self.document.select("html", "body", "main", "div", "form")
        inputs = form.get_all_children("input")
        password = None
        for input in inputs:
            if input.attrs.get("name") == "password_confirmation":
                password = input
                break
        self.assertIsNotNone(
            password,
            msg="Could not find the password1 input",
        )

    def test_form_has_button(self):
        form = self.document.select("html", "body", "main", "div", "form")
        buttons = form.get_all_children("button")
        found_button = None
        for button in buttons:
            if button.inner_text().strip().lower() == "signup":
                found_button = button
                break
        self.assertIsNotNone(
            found_button,
            msg="Could not find the 'Signup' button",
        )

    def test_signup_works(self):
        credentials = {
            "username": "noor",
            "password": "1234abcd.",
            "password_confirmation": "1234abcd.",
        }
        response = self.client.post(reverse("signup"), credentials)
        self.assertEqual(
            response.status_code,
            302,
            msg="Signup does not seem to work",
        )
        self.assertEqual(
            response.headers.get("Location"),
            reverse("home"),
            msg="After signup, it does not redirect to 'home'",
        )

    def test_signup_fails_for_unknown_user(self):
        credentials = {
            "username": "noor",
            "password": "1234abcd.",
            "password_confirmation": "1234abcd.",
        }
        User.objects.create_user("noor", password="abcd1234.")
        with self.assertRaises(IntegrityError):
            self.client.post(reverse("signup"), credentials)
