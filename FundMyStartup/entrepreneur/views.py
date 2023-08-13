from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import startup
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def entreprePro(request):
    mydata = startup.objects.filter(user=request.user)
    context = {'mydata': mydata}
    return render(request, 'entrepreneur_Profile.html', context)