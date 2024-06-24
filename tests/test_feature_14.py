from django.contrib.auth.models import User
from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse

from .utils import Document
from receipts.models import Account


class FeatureTests(TestCase):
    fixtures = ["tests/fixtures/users"]

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.noor)
        self.response = self.client.get("/receipts/accounts/create/")
        self.content = self.response.content.decode("utf-8")
        self.document = Document()
        self.document.feed(self.content)

    @classmethod
    def setUpTestData(cls):
        cls.noor = User.objects.get(username="noor")

    def test_create_account_resolves_to_accounts_create_account(self):
        path = reverse("create_account")
        self.assertEqual(
            path,
            "/receipts/accounts/create/",
            msg="Could not resolve path name 'create_account' to '/receipts/accounts/create/",
        )

    def test_accounts_create_receipt_returns_200(self):
        self.assertEqual(
            self.response.status_code,
            200,
            msg="Did not get the create account page",
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

    def test_form_has_name_input(self):
        form = self.document.select("html", "body", "main", "div", "form")
        inputs = form.get_all_children("input")
        name = None
        for input in inputs:
            if input.attrs.get("name") == "name":
                name = input
                break
        self.assertIsNotNone(
            name,
            msg="Could not find the name input",
        )

    def test_form_has_button(self):
        form = self.document.select("html", "body", "main", "div", "form")
        buttons = form.get_all_children("button")
        found_button = None
        for button in buttons:
            if button.inner_text().strip().lower() == "create":
                found_button = button
                break
        self.assertIsNotNone(
            found_button,
            msg="Could not find the 'Create' button",
        )

    def test_create_receipt_creates_account(self):
        self.client.post(
            "/receipts/accounts/create/",
            {"name": "Test Account", "number": "111111"},
        )
        try:
            Account.objects.get(name="Test Account")
        except Account.DoesNotExist:
            self.fail("Create does not create the Account object")

    def test_create_redirects_to_home(self):
        response = self.client.post(
            "/receipts/accounts/create/",
            {"name": "Test Account", "number": "111111"},
        )
        self.assertEqual(
            response.headers.get("Location"),
            "/receipts/accounts/",
            msg="Create does not redirect to /receipts/accounts",
        )
