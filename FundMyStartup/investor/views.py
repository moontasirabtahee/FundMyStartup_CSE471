from django.shortcuts import render

# Create your views here.

def investPro(request):
    return render(request, 'investorProfile.html')
