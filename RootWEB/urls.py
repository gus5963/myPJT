"""RootWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from RootWEB import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user/', include('userApp.urls')),
]
# include를 사용하는 것은 따로 app을 만들었기 때문이다. 그래서 include() 괄호 안에는 urls로 가도록 한다. 그러면 urls내 있는 urlpatterns를 작동시킨다.
