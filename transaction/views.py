from django.shortcuts import render, redirect

from .forms import TransactionForm
from .models import Transaction

# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction/list.html', {'transactions': transactions})

def add(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            print("폼 유효")
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction:list')
        else:
            print("폼 실패")
    else:
        form = TransactionForm()

    return render(request, 'transaction/add_transaction.html', {'form' : form})