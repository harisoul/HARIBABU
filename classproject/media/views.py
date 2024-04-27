from math import ceil

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import product, posts
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
# def login(request):
#     username = request.POST.get('email')
#     password = request.POST.get('password')
#     print(username, password)
#     user = authenticate(request, username=username, password=password)
#
#     print(user)
#     if user is not None:
#         login(request, user)
#         return redirect('home')
#     else:
#          return redirect('login')
#     return render(request, "login.html")

        # email = request.POST['email']
        # password = request.POST['password']
        #
        # user = authenticate(request,email=email, password=password)
        #
        # if user is not None:
        #     auth.login(request, user)
        #     return redirect('home')
        # else:
        #     return redirect('login')

    # else:
    #     return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = User.objects.create_user(email=email, password=password, username=username)
        user.first_name = fullname
        user.save()

        return redirect('home')
    return render(request, 'signup.html')


def log(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    print(username, password)
    user = authenticate(request, username=username, password=password)

    print(user)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
     return render(request, "login.html")


def home(request):
    products = product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) + (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'home.html', params)


def about(request):
    return render(request, 'aboutus.html')


def profile(request):
    return render(request, 'profile.html')


def postss(request):
    if request.method == 'POST':
        pic = request.FILES['pic']
        bio = request.POST.get('bio')
        user1 = posts.objects.create(pic=pic, bio=bio)
        return redirect('home')
    return render(request, 'post.html')

def settings(request):
    return render(request, 'settings.html')
