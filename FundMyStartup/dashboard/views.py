from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def startup(request):
    if request.method == 'POST':
        title = request.POST.get['title']
        Equity = request.POST.get['Equity']
        funding = request.POST.get['funding']
        Sales= request.POST.get['Sales']
        owner= request.POST.get['Owner']
        profit= request.POST.get['Profit']
        Debts= request.POST.get['Debts']
        return redirect('entreprenuer_Profile.html', title=title, equity=Equity, sales=Sales, owner=owner, profit_margin=profit, debts=Debts, funding_required=funding)

    return render(request, 'startup.html')

def entrepreneur_Profile(request, title, equity, sales, owner, profit_margin, debts, funding_required):
    context = {
        'title': title,
        'equity': equity,
        'sales': sales,
        'owner': owner,
        'profit_margin': profit_margin,
        'debts': debts,
        'funding_required': funding_required,
    }
    return render(request, 'entrepreneur_Profile.html', context)


