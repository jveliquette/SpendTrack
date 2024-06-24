from django.test import SimpleTestCase


class FeatureTests(SimpleTestCase):
    def test_expenses_receipt_created(self):
        try:
            from expenses.settings import INSTALLED_APPS  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find the Django project 'expenses'")

    def test_accounts_app_created(self):
        try:
            from accounts.apps import AccountsConfig  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find the Django app 'accounts'")

    def test_receipts_app_created(self):
        try:
            from receipts.apps import ReceiptsConfig  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find the Django app 'receipts'")

    def test_accounts_app_installed(self):
        try:
            from expenses.settings import INSTALLED_APPS

            self.assertIn("accounts.apps.AccountsConfig", INSTALLED_APPS)
        except ModuleNotFoundError:
            self.fail("Could not find 'accounts' installed in 'expenses'")

    def test_receipts_app_installed(self):
        try:
            from expenses.settings import INSTALLED_APPS

            self.assertIn("receipts.apps.ReceiptsConfig", INSTALLED_APPS)
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts' installed in 'expenses'")
