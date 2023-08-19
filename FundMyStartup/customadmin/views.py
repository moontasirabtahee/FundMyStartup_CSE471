from django.shortcuts import render , redirect

# Create your views here.

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from FundMyStartup.models import feedback
from entrepreneur.models import startup


def adminLogin(request):
    return redirect('adminDashboard')

@login_required(login_url='login')
def adminDashboard(request):
    if request.user.is_superuser:
        feedbackl = feedback.objects.all()
        users = User.objects.all()
        startups = startup.objects.all()
        return render(request, 'adminDashboard.html', {'feedbackl': feedbackl, 'users': users , 'startups': startups})
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
