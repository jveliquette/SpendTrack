from django.test import TestCase
from django.db import models


class FeatureTests(TestCase):
    def test_expense_category_model_exists(self):
        try:
            from receipts.models import ExpenseCategory  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")

    def test_expense_category_model_has_char_name_field(self):
        try:
            from receipts.models import ExpenseCategory

            name = ExpenseCategory.name
            self.assertIsInstance(
                name.field,
                models.CharField,
                msg="ExpenseCategory.name should be a character field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.name'")

    def test_expense_category_model_has_name_with_max_length_50_characters(
        self,
    ):
        try:
            from receipts.models import ExpenseCategory

            name = ExpenseCategory.name
            self.assertEqual(
                name.field.max_length,
                50,
                msg="The max length of ExpenseCategory.name should be 50",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.name'")

    def test_expense_category_model_owner_has_many_to_one_relationship(
        self,
    ):
        try:
            from receipts.models import ExpenseCategory

            owner = ExpenseCategory.owner
            self.assertIsInstance(
                owner.field,
                models.ForeignKey,
                msg="ExpenseCategory should be a foreign key field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.owner'")

    def test_user_model_has_expense_category_related_name_of_categories(
        self,
    ):
        try:
            from receipts.models import ExpenseCategory

            owner = ExpenseCategory.owner
            self.assertEqual(
                owner.field.related_query_name(),
                "categories",
                msg="ExpenseCategory.owner should have a related name of 'categories'",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.owner'")

    def test_expense_category_model_has_owner_related_to_auth_user(
        self,
    ):
        try:
            from receipts.models import ExpenseCategory
            from django.contrib.auth.models import User

            owner = ExpenseCategory.owner
            self.assertEqual(
                owner.field.related_model,
                User,
                msg="ExpenseCategory.owner should be related to the 'auth.User' model",  # noqa: E501
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.owner'")

    def test_expense_category_model_has_owner_has_on_delete_cascade(self):
        try:
            from receipts.models import ExpenseCategory

            owner = ExpenseCategory.owner
            self.assertEqual(
                owner.field.remote_field.on_delete,
                models.CASCADE,
                msg="ExpenseCategory should have CASCADE for on delete",
            )

        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.owner'")

    def test_account_model_exists(self):
        try:
            from receipts.models import Account  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models.Account'")

    def test_account_model_has_char_name_field(self):
        try:
            from receipts.models import Account

            name = Account.name
            self.assertIsInstance(
                name.field,
                models.CharField,
                msg="receipt.name should be a character field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.name'")

    def test_account_model_has_name_with_max_length_100_characters(
        self,
    ):
        try:
            from receipts.models import Account

            name = Account.name
            self.assertEqual(
                name.field.max_length,
                100,
                msg="The max length of receipt.name should be 100",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.name'")

    def test_account_model_has_char_number_field(self):
        try:
            from receipts.models import Account

            name = Account.name
            self.assertIsInstance(
                name.field,
                models.CharField,
                msg="Account.number should be a character field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.name'")

    def test_account_model_has_number_with_max_length_20_characters(
        self,
    ):
        try:
            from receipts.models import Account

            number = Account.number
            self.assertEqual(
                number.field.max_length,
                20,
                msg="The max length of Account.number should be 20",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.name'")

    def test_account_model_owner_has_many_to_one_relationship(
        self,
    ):
        try:
            from receipts.models import Account

            owner = Account.owner
            self.assertIsInstance(
                owner.field,
                models.ForeignKey,
                msg="Account should be a foreign key field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.owner'")

    def test_user_model_has_account_related_name_of_categories(
        self,
    ):
        try:
            from receipts.models import Account

            owner = Account.owner
            self.assertEqual(
                owner.field.related_query_name(),
                "accounts",
                msg="Account.owner should have a related name of 'accounts'",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.owner'")

    def test_account_model_has_owner_related_to_auth_user(
        self,
    ):
        try:
            from receipts.models import Account
            from django.contrib.auth.models import User

            owner = Account.owner
            self.assertEqual(
                owner.field.related_model,
                User,
                msg="Account.owner should be related to the 'auth.User' model",  # noqa: E501
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.owner'")

    def test_account_model_has_owner_has_on_delete_cascade(self):
        try:
            from receipts.models import Account

            owner = Account.owner
            self.assertEqual(
                owner.field.remote_field.on_delete,
                models.CASCADE,
                msg="Account should have CASCADE for on delete",
            )

        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.owner'")

    def test_receipt_model_exists(self):
        try:
            from receipts.models import Receipt  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models.receipt'")

    def test_receipt_model_has_char_vendor_field(self):
        try:
            from receipts.models import Receipt

            vendor = Receipt.vendor
            self.assertIsInstance(
                vendor.field,
                models.CharField,
                msg="receipt.vendor should be a character field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.vendor'")

    def test_receipt_model_has_vendor_with_max_length_200_characters(self):
        try:
            from receipts.models import Receipt

            vendor = Receipt.vendor
            self.assertEqual(
                vendor.field.max_length,
                200,
                msg="The max length of receipt.vendor should be 200",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.vendor'")

    def test_receipt_model_has_decimal_total_field(self):
        try:
            from receipts.models import Receipt

            total = Receipt.total
            self.assertIsInstance(
                total.field,
                models.DecimalField,
                msg="Receipt.total should be a decimal field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.total'")

    def test_receipt_model_has_decimal_total_field_with_decimal_places_3(self):
        try:
            from receipts.models import Receipt

            total = Receipt.total
            self.assertEqual(
                total.field.decimal_places,
                3,
                msg="Receipt.total should have 3 decimal places",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.total'")

    def test_receipt_model_has_decimal_total_field_with_max_digits_10(self):
        try:
            from receipts.models import Receipt

            total = Receipt.total
            self.assertEqual(
                total.field.max_digits,
                10,
                msg="Receipt.total should have a max of 10 digits",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.total'")

    def test_receipt_model_has_decimal_tax_field(self):
        try:
            from receipts.models import Receipt

            tax = Receipt.tax
            self.assertIsInstance(
                tax.field,
                models.DecimalField,
                msg="Receipt.tax should be a decimal field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.tax'")

    def test_receipt_model_has_decimal_tax_field_with_decimal_places_3(self):
        try:
            from receipts.models import Receipt

            tax = Receipt.tax
            self.assertEqual(
                tax.field.decimal_places,
                3,
                msg="Receipt.tax should have 3 decimal places",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.tax'")

    def test_receipt_model_has_decimal_tax_field_with_max_digits_10(self):
        try:
            from receipts.models import Receipt

            tax = Receipt.tax
            self.assertEqual(
                tax.field.max_digits,
                10,
                msg="Receipt.tax should have a max of 10 digits",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.tax'")

    def test_receipt_model_has_date_time_date_field(self):
        try:
            from receipts.models import Receipt

            date = Receipt.date
            self.assertIsInstance(
                date.field,
                models.DateTimeField,
                msg="Receipt.date should be a date time field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.date'")
