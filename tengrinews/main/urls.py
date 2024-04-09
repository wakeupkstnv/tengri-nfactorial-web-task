from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('life', views.life, name='life'),
    path('sport', views.sport, name='sport'),
    path('travel', views.travel, name='travel'),
    path('music', views.music, name='music')
] 