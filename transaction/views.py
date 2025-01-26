from tracemalloc import get_object_traceback

from django.shortcuts import render, redirect, get_object_or_404

from .forms import TransactionForm
from .models import Transaction
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction/list.html', {'transactions': transactions})

@login_required
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

@login_required
def delete(request, pk):
    item = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('transaction:list')
    return render(request, 'transaction/delete_transaction.html', {'transaction': item})

def sum(request):
    total = 0
    for transaction in Transaction.objects.all():
        total += transaction.amount
    return total;