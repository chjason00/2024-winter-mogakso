from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        # 관리자 계정 확인 및 리다이렉트
        if request.user.is_staff:  # 관리자 권한 여부 확인
            print("이 계정은 관리자 계정입니다.")
            return redirect('/admin/')  # Django admin URL로 리다이렉트
        message = "{}님, 환영합니다!".format(request.user.username)
    else:
        message = "로그인이 필요합니다."
    context = {'message': message}
    return render(request, 'home/home.html', context)