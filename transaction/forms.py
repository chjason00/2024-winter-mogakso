# forms.py
from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'date']  # 폼에서 사용할 필드
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # HTML5의 날짜 선택기 사용
        }