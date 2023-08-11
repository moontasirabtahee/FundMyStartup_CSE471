from django.shortcuts import render, redirect
from .models import Idea


def startup(request):
    if request.method == 'POST':
        title = request.POST['title']
        Equity = request.POST['Equity']
        funding = request.POST['funding']
        Sales= request.POST['Sales']
        owner= request.POST['Owner']
        profit= request.POST['Profit']
        Debts= request.POST['Debts']

        # Create a new Idea instance and save it to the database
        new_idea = Idea(title=title, Equity=Equity, funding=funding, Sales=Sales, owner=owner, profit=profit, Debts=Debts)
        new_idea.save()
        return redirect('startup')

    # Retrieve and display submitted ideas for the logged-in entrepreneur
    submitted_ideas = Idea.objects.filter(entrepreneur=request.user)  # Assuming you have a user field in the Idea model
    return render(request, 'startup.html', {'submitted_ideas': submitted_ideas})

