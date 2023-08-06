from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
# from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Write a Registration function for my project
def registration(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['ages']
        email = request.POST['emails']
        phone = request.POST['phone']
        NID = request.POST['NID']
        if request.POST['pass1'] == request.POST['pass2']:
            password = request.POST['password1']
            user = User.objects.create_user(first_name=fname, last_name=lname, age=age, email=email, phone=phone, NID=NID, password=password)
            user.save()
            messages.success(request, 'You have successfully registered')
            return redirect('login')

        else:
            messages.error(request, 'Password does not match')
            return redirect('registration')

    else:
        return render(request, 'registration.html')

# Write a Login function for my project
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # user = auth.authenticate(email=email, password=password)
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

# Write a Logout function for my project
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('index')

#Write a funtion to update profile info
@login_required(login_url='login')
def updateprofile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.age = request.POST['ages']
        user.email = request.POST['emails']
        user.phone = request.POST['phone']
        user.submits = request.POST['submits']
        user.website = request.POST['website']
        if request.POST['pass1'] == request.POST['pass2']:
            user.password = request.POST['pass1']
            user.save()
            messages.success(request, 'You have successfully updated your profile')
            return redirect('profile')
        else:
            messages.error(request, 'Password does not match')
            return redirect('updateprofile')
    else:
        return render(request, 'update.html')



