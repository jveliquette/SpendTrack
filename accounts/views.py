from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.forms import LogInForm, SignUpForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LogInForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("login")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirmation']
            if password == password_confirmation:
                # Create new user with those values and save it to a variable
                user = User.objects.create_user(
                    username,
                    password=password
                )
                # Login user with user that was just created
                login(request, user)
                return redirect("home")
            else:
                form.add_error("password", "Passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
