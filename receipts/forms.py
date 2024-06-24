from django.forms import ModelForm
from receipts.models import Receipt, ExpenseCategory, Account

class CreateReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]

class CreateCategory(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
            "name",
        ]

class CreateAccount(ModelForm):
    class Meta:
        model = Account
        fields = [
            "name",
            "number",
        ]
