from django.shortcuts import render

# Create your views here.
def entreprePro(request):
    return render(request, 'entrepreneur_Profile.html')