from django.urls import path, include
from userApp import views


urlpatterns = [
    # http://127.0.0.1:8000/user/index
    path('index/', views.index, name = 'userIndex'),
    path('login/', views.login),
    path('list/', views.list),
    path('detail/', views.detail),
    path('signUp/', views.signUp),
    path('join/', views.join),
    path('logout/', views.logout),

    # views 에 있는 redirect에서 사용할 수 있는 name을 적어주되 values는 url과 같도록 해야한다.
]

