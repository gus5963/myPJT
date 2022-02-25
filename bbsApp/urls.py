from django.urls import path, include
from bbsApp import views


urlpatterns = [
    path('index/', views.index, name = 'bbsIndex'),
    path('createForm/', views.createForm, name = 'bbsCreateForm'),
    path('bbsWrite/', views.bbsWrite, name='bbsWrite'),
    path('bbsRead/', views.bbsRead, name='bbsRead'),
    path('bbsRemove/', views.bbsRemove, name='bbsRemove'),
    path('bbsUpdate/', views.bbsUpdate, name='bbsUpdate'),
    path('bbsSearch/', views.bbsSearch, name='bbsSearch')
]
