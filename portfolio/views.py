from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.
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