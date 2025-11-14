from django.urls import path
from . import views

app_name = 'cafeteria'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('events/', views.events, name='events'),
    path('branches/', views.branches, name='branches'),
    path('comment/', views.comment, name='comment'),
]
