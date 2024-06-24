from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.models import User
from django.utils import timezone


class FeatureTests(TestCase):
    def setUp(self):
        self.client = Client()

    def create_test_receipts(self):
        noors_category = ExpenseCategory.objects.create(
            name="Category 1", owner=self.noor
        )
        noors_account = Account.objects.create(
            name="Noors Account", number="100010101", owner=self.noor
        )
        noors_receipt = Receipt.objects.create(
            vendor="ZZZZZZ",
            total=100,
            tax=20,
            date=timezone.now(),
            category=noors_category,
            account=noors_account,
            purchaser=self.noor,
        )
        alishas_category = ExpenseCategory.objects.create(
            name="Category 2", owner=self.alisha
        )
        alishas_account = Account.objects.create(
            name="Alisa's Account", number="100100101", owner=self.alisha
        )
        alishas_receipt = Receipt.objects.create(
            vendor="YYYYYY",
            total=300,
            tax=40,
            date=timezone.now(),
            category=alishas_category,
            account=alishas_account,
            purchaser=self.alisha,
        )
        return noors_receipt, alishas_receipt

    def login(self):
        self.noor_credentials = {"username": "noor", "password": "1234abcd."}
        self.noor = User.objects.create_user(**self.noor_credentials)
        self.alisha = User.objects.create_user(
            username="alisha", password="1234abcd."
        )
        self.client.post(reverse("login"), self.noor_credentials)

    def test_receipts_list_is_protected(self):
        response = self.client.get("/receipts/")
        self.assertEqual(
            response.status_code,
            302,
            msg="Receipt list view is not protected",
        )
        self.assertTrue(
            response.headers.get("Location").startswith(reverse("login")),
            msg="Receipt list view did not redirect to login page",
        )

    def test_receipts_list_only_returns_purchasers_receipts(self):
        # Arrange
        self.login()
        noors_receipt, alishas_receipt = self.create_test_receipts()

        # Act
        response = self.client.get("/receipts/")
        # Assert
        self.assertNotContains(
            response,
            alishas_receipt.vendor,
            msg_prefix=f"Found a receipt on the page that did not belong to the logged in user.",
            html=True,
        )

    def test_receipts_list_shows_vendor(self):
        # Arrange
        self.login()
        noors_receipt, _ = self.create_test_receipts()

        # Act
        response = self.client.get("/receipts/")
        # Assert
        self.assertContains(
            response,
            noors_receipt.vendor,
            msg_prefix=f"Did not find the vendor in the HTML",
            html=True,
        )

    def test_receipts_list_shows_total(self):
        # Arrange
        self.login()
        noors_receipt, _ = self.create_test_receipts()

        # Act
        response = self.client.get("/receipts/")
        # Assert
        self.assertContains(
            response,
            "%.3f" % noors_receipt.total,
            msg_prefix=f"Did not find the total in the HTML",
            html=True,
        )

    def test_receipts_list_shows_tax(self):
        # Arrange
        self.login()
        noors_receipt, _ = self.create_test_receipts()

        # Act
        response = self.client.get("/receipts/")
        # Assert
        self.assertContains(
            response,
            "%.3f" % noors_receipt.tax,
            msg_prefix="Did not find the tax in the HTML",
            html=True,
        )

    def test_receipts_list_shows_category_name(self):
        # Arrange
        self.login()
        noors_receipt, _ = self.create_test_receipts()

        # Act
        response = self.client.get("/receipts/")
        # Assert
        self.assertContains(
            response,
            noors_receipt.category.name,
            msg_prefix="Did not find the category name in the HTML",
            html=True,
        )

    def test_receipts_list_shows_account_name(self):
        # Arrange
        self.login()
        noors_receipt, _ = self.create_test_receipts()

        # Act
        response = self.client.get("/receipts/")
        # Assert
        self.assertContains(
            response,
            noors_receipt.account.name,
            msg_prefix="Did not find the account name in the HTML",
            html=True,
        )
