from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.messages import get_messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


# This is the Home Page
@login_required(login_url='login/')
def home(request):
    return render(request, 'index.html')

# This is the SignUp Page

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # print(username,email,password,password2)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is Taken")
                return redirect(signup)
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username is Taken")
                return redirect(signup)
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()

                # Log the user in and redirect to the Home page

                # create a Profile object for the new User
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id,name=username,email=email,password=password)
                new_profile.save()
                return redirect(login)
        else:
            messages.info(request, "Passwords Don't Match.")
            return redirect(signup)
    else:
        return render(request, 'signup.html')


# This is the Login Page

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            messages.info(request, "Invalid Credentials")
            return redirect(login)
    else:
        return render(request, 'login.html')


# The logout
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect(login)
