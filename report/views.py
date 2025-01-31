import matplotlib
matplotlib.use('Agg') # macOS 상에서 그래프를 GUI로 렌더링할 경우 오류가 발생하므로, 이 코드를 추가로 넣어서 백그라운드에서 렌더링하게 수정

from django.shortcuts import render
from transaction.models import Transaction
from django.contrib.auth.decorators import login_required
from matplotlib import pyplot as plt

import os
from django.conf import settings

# Create your views here.
# views.py

def generate_graph(user):
    """그래프를 생성하고 이미지 파일 경로를 반환"""
    transactions = Transaction.objects.filter(user=user)

    print(f"📌 Debug: user = {user}, user type = {type(user)}")  # 🚀 Debugging 추가

    # 🚨 로그 추가해서 데이터가 정상적으로 존재하는지 확인
    print(f"📌 Found {len(transactions)} transactions for user: {user}")

    y = [t.amount for t in transactions]
    x = [t.date.strftime('%Y-%m-%d') for t in transactions]  # 날짜 포맷 변환

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o', color='blue', label='Transaction')

    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Transaction Report")

    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Static 디렉토리에 저장
    graph_dir = os.path.join(settings.BASE_DIR, 'static', 'graphs')
    os.makedirs(graph_dir, exist_ok=True)

    graph_path = os.path.join(graph_dir, 'transaction_report.png')

    # 🚨 파일 저장 테스트 로그 추가
    print(f"📌 Saving graph to: {graph_path}")

    try:
        plt.savefig(graph_path)
        print("✅ Graph saved successfully!")
    except Exception as e:
        print(f"❌ Graph save failed: {e}")  # 오류 메시지 확인
    finally:
        plt.close()

    return settings.STATIC_URL + 'graphs/transaction_report.png'

@login_required
def report_overview(request):
    """리포트 개요를 보여주면서 그래프도 생성"""
    transactions = Transaction.objects.filter(user=request.user)
    total = sum(t.amount for t in transactions)

    # 🚀 여기에서 `generate_graph()`를 실행해서 그래프 생성
    graph_path = generate_graph(request.user)

    return render(request, 'report/overview.html', {
        'total': total,
        'graph_path': graph_path
    })