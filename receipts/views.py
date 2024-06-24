from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import CreateReceiptForm, CreateCategory, CreateAccount

# Create your views here.
@login_required
def receipt_list(request):
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipt
    }
    return render(request, "receipts/list.html", context)

@login_required
def create_receipt(request):
    if request.method == "POST":
        form = CreateReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = CreateReceiptForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)

@login_required
def category_list(request):
    expense_categories = ExpenseCategory.objects.filter(owner=request.user)
    data = []
    for category in expense_categories:
        receipt_count = Receipt.objects.filter(category=category).count()
        data.append({
            "name": category.name,
            "receipt_count": receipt_count,
        })

    context = {
        "data": data,
    }
    return render(request, "receipts/category.html", context)

@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    data = []
    for account in accounts:
        receipt_count = Receipt.objects.filter(account=account).count()
        data.append({
            "name": account.name,
            "number": account.number,
            "receipt_count": receipt_count,
        })

    context = {
        "data": data,
    }
    return render(request, "receipts/account.html", context)

@login_required
def create_category(request):
    if request.method == "POST":
        form = CreateCategory(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = CreateCategory()
    context = {
        "form": form
    }
    return render(request, "receipts/create_category.html", context)

@login_required
def create_account(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect("account_list")
    else:
        form = CreateAccount()
    context = {
        "form": form
    }
    return render(request, "receipts/create_account.html", context)
