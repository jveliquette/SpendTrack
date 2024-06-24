from django.contrib import admin
from django.test import TestCase


class FeatureTests(TestCase):
    def test_receipt_registered_with_admin(self):
        try:
            from receipts.models import Receipt

            self.assertTrue(
                admin.site.is_registered(Receipt),
                msg="receipts.models.Receipt is not registered with the admin",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Receipt'")

    def test_category_registered_with_admin(self):
        try:
            from receipts.models import ExpenseCategory

            self.assertTrue(
                admin.site.is_registered(ExpenseCategory),
                msg="receipts.models.ExpenseCategory is not registered with the admin",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")

    def test_account_registered_with_admin(self):
        try:
            from receipts.models import Account

            self.assertTrue(
                admin.site.is_registered(Account),
                msg="receipts.models.Account is not registered with the admin",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
