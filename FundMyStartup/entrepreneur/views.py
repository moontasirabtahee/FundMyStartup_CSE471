
from .models import startup
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .models import startup

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
        return redirect('entreprePro')
    else:
        return render(request, 'startup.html')


@login_required(login_url='login')
def entreprePro(request):
    if startup.objects.filter(user=request.user).exists():
        start = startup.objects.filter(user=request.user)
        print(start)
        return render(request, 'entrepreneur_Profile.html', {'mydata': start})
    else:
        return redirect('startup')

@login_required(login_url='login')
def editstart(request):
    if startup.objects.filter(user=request.user).exists():
        if request.method == 'POST':
            title = request.POST['title']
            Equity = request.POST['Equity']
            funding = request.POST['funding']
            Sales = request.POST['Sales']
            owner = request.POST['owner']
            profit = request.POST['profit']
            Debts = request.POST['debts']
            user = request.user

            start = startup.objects.filter(user=request.user).update(user=user, title=title, Equity=Equity, funding=funding,
                                                                      Sales=Sales, owner=owner, profit=profit,
                                                                        debts=Debts)



            print('startup updatesd')
            return redirect('entreprePro')
        else:
            startupl = startup.objects.filter(user=request.user)
            return render(request, 'editstartup.html', {'startups': startupl})
    else:
        return redirect('entreprePro')

