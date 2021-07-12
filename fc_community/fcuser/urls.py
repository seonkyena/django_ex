from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),  # 함수를 가져옴
    path('login/', views.login),
    path('logout/', views.logout),
    path('home/', views.home),
]