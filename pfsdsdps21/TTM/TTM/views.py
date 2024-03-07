from django.shortcuts import render


def homePage(request):
    return render(request, "index.html")


def loginPage(request):
    return render(request, "login.html")


def contactPage(request):
    return render(request, "contactus.html")


def aboutPage(request):
    return render(request, "aboutus.html")


def registrationPage(request):
    return render(request, "register.html")
