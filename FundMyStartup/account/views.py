from django.shortcuts import render

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')

def updateprofile(request):
    return render(request,'update.html')

def logout(request):
    pass
