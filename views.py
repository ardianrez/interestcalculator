from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def calculate(request):
    if request.method == 'POST':
        principle = float(request.POST.get('principle'))
        rate = float(request.POST.get('rate'))
        time = float(request.POST.get('time'))

        # Calculate interest and total amount
        interest = (principle * rate * time) / 100
        total_amount = principle + interest

        context = {'interest': interest, 'total_amount': total_amount}
        return render(request, 'result.html', context)

    return HttpResponse('Error: Invalid request method')