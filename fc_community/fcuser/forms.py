from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '학번을 입력해주세요.'
        },
        max_length=32, label="학번")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()  # super를 써서 상위 함수 먼저 호출
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '등록되지 않은 ID입니다.')
                return

            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
            else:
                self.user_id = fcuser.id
