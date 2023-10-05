from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticlesList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('endorse/<slug:slug>', views.ArticlesEndorsement.as_view(), name="articles_endorsement"),
]
