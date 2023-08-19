from django.shortcuts import render
from entrepreneur.models import startup
# Create your views here.

def investPro(request):
    startups = startup.objects.all()
    return render(request, 'investorProfile.html', {'startups':startups})
