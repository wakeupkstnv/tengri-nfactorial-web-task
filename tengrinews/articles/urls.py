from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_home, name='articles'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article-detail')
] 