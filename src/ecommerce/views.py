from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import ContactForm, LoginForm, RegisterForm

def about(request):
    context = {
        "title":"About Page",
        "content":" Welcome to the about page."
    }
    return render(request, "about.html", context)

def homepage(request):
    return render(request, "homepage.html")

def contact(request):
    contact_form = ContactForm()
    context = {
        "title": "Contact",
        "content": "",
        "form": contact_form
    }
    if request.method == "POST":
        print(request.POST.get('fname'))
        print(request.POST.get('lname'))
        print(request.POST.get('eaddress'))
        print(request.POST.get('tel'))
        print(request.POST.get('message'))
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        new_user  = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)
