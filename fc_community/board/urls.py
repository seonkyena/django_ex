from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.board_detail),
    path('list/', views.board_list),  # 함수를 가져옴
    path('write/', views.board_write),
]
