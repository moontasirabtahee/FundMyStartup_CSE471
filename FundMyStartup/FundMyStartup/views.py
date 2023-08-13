from django.shortcuts import render
from .models import feedback
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feback = request.POST.get('message')
        back = feedback(name=name, email=email, feedback=feback)
        back.save()
        print('feedback saved')
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
