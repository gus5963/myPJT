from django.urls import path, include
from staticApp import views


urlpatterns = [
    path('index/', views.index, name = 'staticIndex'),
    path('line/', views.line, name = 'staticLine'),
    path('bar/', views.bar, name = 'staticBar'),
]
