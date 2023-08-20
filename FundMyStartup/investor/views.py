from django.shortcuts import render
from entrepreneur.models import startup
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import investedStartup



@login_required(login_url='login')
def investPro(request):
    if request.method == 'POST':
        user = request.user
        startupst = request.POST['startup_id']
        startupst = startup.objects.get(id=startupst)
        amount = request.POST['amount']

        invest = investedStartup.objects.create(user=user, startup=startupst, amount=amount)
        invest.save()
        print('invested')

        return render(request, 'investorProfile.html')
    else:
        startups = startup.objects.all()
        return render(request, 'investorProfile.html', {'startups':startups})
