from syslog import LOG_INFO

from django.shortcuts import render
from transaction.models import Transaction
from django.contrib.auth.decorators import login_required
from matplotlib import pyplot as plt
from io import BytesIO
import base64

# Create your views here.
# views.py
@login_required
def report_overview(request):
    transactions = Transaction.objects.filter(user=request.user)
    total = sum(t.amount for t in transactions)
    return render(request, 'report/overview.html', {'total': total})

def report_graph(request):
    transactions = Transaction.objects.filter(user=request.user)
    y = [t.amount for t in transactions]
    x = [t.date for t in transactions]
    # Create a line plot
    plt.plot(x, y, marker='o', color='blue', label='Line')

    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    plt.title("Line Plot Example")

    plt.legend()

    # 그래프를 파일로 저장
    file_path = 'static/graphs/transaction_report.png'
    plt.savefig(file_path)
    plt.close()

    # HTML에 렌더링
    return render(request, 'report/overview.html', {'graph_path': file_path})

