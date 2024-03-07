import django.http
from django.shortcuts import render
from .models import Register
from django.contrib import messages


def ttmhome(request):
    return render(request, "ttmhome.html")


def loginfail(request):
    return render(request, "loginfail.html")


def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwdd = request.POST["pwd"]
        flag = Register.objects.filter(username=name, password=pwdd).values()
        if flag:  # flag isn't empty
            if name == "Keerthi":  # amruthavarshini is admin
                return render(request, "adminhome.html")

        if flag:
            return render(request, "ttmhome.html")
        else:
            return render(request, "loginfail.html")


def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username existing...")
                return render(request, "register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name, address=addr, email=email, phno=phno, username=uname,
                                               password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
    else:
        messages.info(request, "password is not matching...")
        return render(request, "register.html")