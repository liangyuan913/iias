from django.urls import path
from notice import views


app_name = 'notice'
urlpatterns =[
        path('', views.notice, name='notice'),
        path('noticeCreate/', views.noticeCreate, name='noticeCreate'),
        path('noticeRead/<int:noticeId>/', views.noticeRead, name='noticeRead')
    ]

