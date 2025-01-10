from django.shortcuts import render
from .models import Transaction

# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction/list.html', {'transactions': transactions})