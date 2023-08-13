from django.shortcuts import render
from .models import feedback
# Create your views here.
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feback = request.POST.get('message')
        back = feedback(name=name, email=email, feedback=feback)
        back.save()
        messages.success(request, 'Thank you for your feedback')
        print('feedback saved')
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
