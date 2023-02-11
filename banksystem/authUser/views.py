from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    if request.user.is_authenticated:
        return redirect('main')
    
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        birthday = request.POST["birthday"]
        email = request.POST["email"]
        phone = request.POST["phone"]   
        password = request.POST["password"]

        if Customer.objects.filter(email=email).exists():
            return render(request , 'register.html', {
                'error' : 'Email is already using!'
            })
        else:
            customer = Customer.objects.create_user(
                username = email,
                email = email,
                first_name = first_name,
                last_name = last_name,
                password = password,
                BirthdayDate = str(birthday),
                PhoneNumber = str(phone),
            )

            customer.save()
            customer = authenticate(request, username= email, password=password)

            login(request, customer)

            return redirect('main')

    return render(request , 'register.html')

def loginreq(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass"]

        user = authenticate(request, username = email, password = password)

        if user is not None:
            login(request, user)
            print("here")
            return redirect('main')
        else:
            print("patladin aq")
            return render(request, 'login.html',{
                'error':'Email or Password is wrong',
            })

    return render(request, "login.html")

