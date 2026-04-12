from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def login_page(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "1234":
            message = "Login Successfully"
        else:
            message = "Login Failed"

    return render(request, "accounts/login.html", {"message": message})