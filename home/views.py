from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        message = "{}님, 환영합니다!".format(request.user.username)
    else:
        message = "로그인이 필요합니다."
    return render(request, 'home/home.html', {'message': message})