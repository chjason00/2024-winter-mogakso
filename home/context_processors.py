# 이 파일은 모든 템플릿에 공통적으로 필요한 데이터를 html로 전해야 할 때, 이 파일을 작성해줌으로써 반복적인 코드작성을 줄인다.
# 사용하기 전 settings.py의 context 란에 반드시 이 파일을 추가한다.
# 여기서는 user_message를 통해 로그인 중인 유저 정보를 메세지로 반환하고자 하면, 반환하는 변수명을 써주면 된다.

def user_message(request):
    if request.user.is_authenticated:
        return {'message': f"{request.user.username}님, 환영합니다!"}
    return {'message': "로그인이 필요합니다."}