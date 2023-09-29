from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticlesList.as_view(), name='home'),
]
