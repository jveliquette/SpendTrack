from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from .utils import Document
from receipts.models import Account, ExpenseCategory, Receipt


class FeatureTests(TestCase):
    fixtures = [
        "tests/fixtures/users",
        "tests/fixtures/accounts",
        "tests/fixtures/categories",
    ]

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.noor)
        self.response = self.client.get("/receipts/create/")
        self.content = self.response.content.decode("utf-8")
        self.document = Document()
        self.document.feed(self.content)

    @classmethod
    def setUpTestData(cls):
        cls.noor = User.objects.get(username="noor")

    def test_create_receipt_resolves_to_create_receipt(self):
        path = reverse("create_receipt")
        self.assertEqual(
            path,
            "/receipts/create/",
            msg="Could not resolve path name 'create_receipt' to '/receipts/create/",
        )

    def test_create_receipt_returns_200(self):
        self.assertEqual(
            self.response.status_code,
            200,
            msg="Did not get the create receipt page",
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

    def test_form_has_vendor_input(self):
        form = self.document.select("html", "body", "main", "div", "form")
        inputs = form.get_all_children("input")
        vendor = None
        for input in inputs:
            if input.attrs.get("name") == "vendor":
                vendor = input
                break
        self.assertIsNotNone(
            vendor,
            msg="Could not find the vendor input",
        )

    def test_form_has_total_input(self):
        form = self.document.select("html", "body", "main", "div", "form")
        inputs = form.get_all_children("input")
        total = None
        for input in inputs:
            if input.attrs.get("name") == "total":
                total = input
                break
        self.assertIsNotNone(
            total,
            msg="Could not find the total input",
        )

    def test_form_has_tax_input(self):
        form = self.document.select("html", "body", "main", "div", "form")
        inputs = form.get_all_children("input")
        tax = None
        for input in inputs:
            if input.attrs.get("name") == "tax":
                tax = input
                break
        self.assertIsNotNone(
            tax,
            msg="Could not find the tax input",
        )

    def test_form_has_date_input(self):
        form = self.document.select("html", "body", "main", "div", "form")
        inputs = form.get_all_children("input")
        date = None
        for input in inputs:
            if input.attrs.get("name") == "date":
                date = input
                break
        self.assertIsNotNone(
            date,
            msg="Could not find the date input",
        )

    def test_form_has_account_select(self):
        form = self.document.select("html", "body", "main", "div", "form")
        selects = form.get_all_children("select")
        accounts = None
        for select in selects:
            if select.attrs.get("name") == "account":
                accounts = select
                break
        self.assertIsNotNone(
            accounts,
            msg="Could not find the accounts select",
        )

    def test_form_has_category_select(self):
        form = self.document.select("html", "body", "main", "div", "form")
        selects = form.get_all_children("select")
        categories = None
        for select in selects:
            if select.attrs.get("name") == "category":
                categories = select
                break
        self.assertIsNotNone(
            categories,
            msg="Could not find the category select",
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

    def test_create_receipt_creates_receipt(self):
        category = ExpenseCategory.objects.first()
        account = Account.objects.first()

        self.client.post(
            reverse("create_receipt"),
            {
                "vendor": "ZZZZZZ",
                "total": 100,
                "tax": 10,
                "date": timezone.now(),
                "category": category.id,
                "account": account.id,
            },
        )
        try:
            Receipt.objects.get(vendor="ZZZZZZ")
        except Receipt.DoesNotExist:
            self.fail("Create does not create the Receipt object")

    def test_create_redirects_to_home(self):
        category = ExpenseCategory.objects.first()
        account = Account.objects.first()
        response = self.client.post(
            "/receipts/create/",
            {
                "vendor": "ZZZZZZ",
                "total": 100,
                "tax": 10,
                "date": timezone.now(),
                "category": category.id,
                "account": account.id,
            },
        )
        self.assertEqual(
            response.headers.get("Location"),
            reverse("home"),
            msg="Create does not redirect to home",
        )
