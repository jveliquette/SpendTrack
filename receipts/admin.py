from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt

# Register your models here.
@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner",
    ]

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "number",
        "owner",
    ]

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = [
        "vendor",
        "total",
        "tax",
        "date",
        "purchaser",
        "category",
        "account",
    ]
