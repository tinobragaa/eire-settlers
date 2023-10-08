from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticlesList.as_view(), name='home'),
    path('profile/', views.MemberProfile.as_view(), name="member_profile"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path(
        'endorse/<slug:slug>',
        views.ArticlesEndorsement.as_view(),
        name="articles_endorsement"
        ),
    path(
        'save/<slug:slug>',
        views.SavedArticle.as_view(),
        name="saved_article"
        ),
]

