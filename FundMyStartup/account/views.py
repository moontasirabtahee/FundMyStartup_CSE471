from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .models import profile
from django.contrib.auth.models import User


def registration(request):
    if request.method == 'POST':

        username = request.POST['username']
        user_type = request.POST['user_type']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        dob = request.POST['dob']
        nid_number = request.POST['nid_number']
        nid_image = request.POST['nid_image']

        if request.POST['password'] == request.POST['password2']:
            password = request.POST['password']
            user = User.objects.create_user(username=username, password=password, email=email, first_name=fname,
                                            last_name=lname)
            user.save()
            pro = profile.objects.create(user=user, user_type=user_type, phone=phone, address=address, dob=dob,
                                         nid_number=nid_number, nid_image=nid_image)
            pro.save()
            print('user created')
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            print('password does not match')
            messages.error(request, 'Password does not match')
            return redirect('registration')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            print('user found')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_superuser:
                    print('admin logged in')
                    auth_login(request, user)
                    return redirect('adminLogin')
                auth_login(request, user)
                print('user logged in')
                if profile.objects.filter(user=request.user).exists():
                    print('user profile found')
                    user_type = profile.objects.get(user=request.user).user_type
                    print(user_type)
                    if user_type == 'investor':
                        return redirect('investor_Profile')
                    elif user_type == 'entrepreneur':
                        return redirect('entreprePro')

            else:
                print('user not found or password does not match')
                messages.error(request, 'Invalid username or password')
                return redirect('login')
        else:
            print('user not found ')
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')



@login_required(login_url='login')
def updateprofile(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()

        profile.objects.filter(user=request.user).update(phone=request.POST['phone'], address=request.POST['address'],
                                                         dob=request.POST['dob'], nid_number=request.POST['nid_number'],
                                                         nid_image=request.FILES['nid_image'])
        messages.success(request, 'Profile updated successfully')
        return redirect('updateprofile')
    else:
        return render(request, 'updateprofile.html')


def logout(request):
    auth_logout(request)
    return redirect('login')
