from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'date', 'memo']  # 폼에서 사용할 필드
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # HTML5의 날짜 선택기 사용
        }

    # 필드에 대한 데이터 검증이 필요한 경우, clean_<fieldname>의 메소드 생성
    # 전체 폼을 한번에 검증하려면, clean()으로 작성
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            # 이렇게 하면 템플릿 자체에서 사용자단에 메세지를 자동으로 렌더링 및 출력
            raise forms.ValidationError('금액을 다시 입력하세요.')
        return amount  # 검증된 값 반환


    '''
    # 전체 form을 한번에 검증하는 로직
    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        date = cleaned_data.get('date')

        # 검증 로직: 특정 날짜에는 amount가 100보다 커야 함
        if date and amount and date == '2025-01-01' and amount < 100:
            raise forms.ValidationError('On 2025-01-01, amount must be at least 100.')
        return cleaned_data
    '''