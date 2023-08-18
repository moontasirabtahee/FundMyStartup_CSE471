from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import startup

@login_required(login_url='login')
def Createstartup(request):
    if request.method == 'POST':
        title = request.POST['title']
        Equity = request.POST['Equity']
        funding = request.POST['Funding']
        Sales= request.POST['Sales']
        owner= request.POST['Owner']
        profit= request.POST['Profit']
        Debts= request.POST['Debts']
        user = request.user

        start = startup(user = user ,title=title, Equity=Equity, funding=funding, Sales=Sales, owner=owner, profit=profit, debts=Debts)
        start.save()
        print('startup created')
        return render(request, 'entrepreneur_Profile.html')
    else:
        return render(request, 'startup.html')

def entreprePro(request):
    current_user=request.user
    mydata = startup.objects.all(user=current_user)
    context = {'mydata': mydata}
    return render(request, 'entrepreneur_Profile.html', context)




