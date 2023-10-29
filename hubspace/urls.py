from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticlesList.as_view(), name='home'),
    path('articles/', views.ArticlesList.as_view(), name='articles_list'),
    path('profile/', views.MemberProfile.as_view(), name="member_profile"),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('delete-profile/', views.delete_profile, name="delete_profile"),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),
    path('edit-comment/<int:comment_id>/', views.edit_comment, name="edit_comment"),
    path('report-comment/<int:pk>/', views.ReportComment.as_view(), name="report_comment"),
    path('create-article/', views.CreateArticle.as_view(), name="create_article"),
    path('edit-article/<slug:slug>/', views.EditArticle.as_view(), name='edit_article'),
    path('delete/<slug:slug>/', views.DeleteArticle.as_view(), name='delete_article'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('member-articles/<str:user>/', views.MemberArticles.as_view(), name='member_articles'),
    path('saved-articles/<str:user>/', views.SavedArticles.as_view(), name='saved_articles'),
    path('endorse/<slug:slug>', views.ArticlesEndorsement.as_view(), name="articles_endorsement"),
    path('save/<slug:slug>', views.SavedArticle.as_view(), name="saved_article"),
]
