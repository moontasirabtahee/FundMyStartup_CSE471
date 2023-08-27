from django.shortcuts import render , redirect

# Create your views here.

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from FundMyStartup.models import feedback
from entrepreneur.models import startup
from communication.models import Room, Message


def adminLogin(request):
    return redirect('adminDashboard')

@login_required(login_url='login')
def adminDashboard(request):
    if request.user.is_superuser:
        feedbackl = feedback.objects.all()
        users = User.objects.all()
        startups = startup.objects.all()
        rooms = Room.objects.all()
        chats = Message.objects.all()



        return render(request, 'adminDashboard.html', {'feedbackl': feedbackl, 'users': users , 'startups': startups, "rooms": rooms , "chats": chats})
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')

def UserList(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'userList.html', {'users': users})
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')

def Rooms(request):
    if request.user.is_superuser:
        rooms = Room.objects.all()
        return render(request, 'roomname.html', {'rooms':rooms})
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')

def Messages(request):
    if request.user.is_superuser:
        chats = Message.objects.all()
        return render(request, 'chat.html', {'chats': chats})
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')

def feedbacklist(request):
    if request.user.is_superuser:
        feedbackl = feedback.objects.all()
        return render(request, 'feedbacklist.html', {'feedbackl': feedbackl})

    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')

@login_required(login_url='login')
def adminLogout(request):
    auth.logout(request)
    return redirect('login')

def deleteFeedback(request, id):
    if request.user.is_superuser:
        feedback.objects.filter(id=id).delete()
        messages.success(request, 'Feedback deleted successfully')
        return redirect('feedbacklist')
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')



def deleteStartup(request, id):
    if request.user.is_superuser:
        startup.objects.filter(id=id).delete()
        messages.success(request, 'Startup deleted successfully')
        return redirect('adminDashboard')
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')

def editStartup(request, id):
    if request.user.is_superuser :
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']
            image = request.FILES['image']
            amount = request.POST['amount']
            startup.objects.filter(id=id).update(name=name, description=description, image=image, amount=amount)
            messages.success(request, 'Startup updated successfully')
            return redirect('adminDashboard')
        else:
            startupl = startup.objects.get(id=id)
            return render(request, 'editStartup.html', {'startup': startupl})
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')

def editUser(request, id):
    if request.user.is_superuser or id == request.user.id:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            User.objects.filter(id=id).update(first_name=first_name, last_name=last_name, email=email)
            messages.success(request, 'User updated successfully')
            return redirect('userList')
        else:
            user = User.objects.get(id=id)
            return render(request, 'editUser.html', {'user': user})
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')


def deleteUser(request, id):
    if request.user.is_superuser:
        User.objects.filter(id=id).delete()
        messages.success(request, 'User deleted successfully')
        return redirect('userList')
    else:
        messages.error(request, 'You are not authorized to view this page')
        return redirect('login')

