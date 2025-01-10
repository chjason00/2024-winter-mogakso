from django.shortcuts import render
from transaction.models import Transaction

# Create your views here.
# views.py
def report_overview(request):
    transactions = Transaction.objects.filter(user=request.user)
    total = sum(t.amount for t in transactions)
    return render(request, 'report/overview.html', {'total': total})