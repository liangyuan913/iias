from django.urls import path
from declaration import views


app_name = 'declaration'
urlpatterns =[
        path('', views.declaration, name='declaration'),
    ]

