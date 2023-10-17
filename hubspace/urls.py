from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticlesList.as_view(), name='home'),
    path('profile/', views.MemberProfile.as_view(), name="member_profile"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_profile/', views.delete_profile, name="delete_profile"),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),
    path('edit-comment/<int:comment_id>/', views.edit_comment, name="edit_comment"),
    path('report_comment/<int:pk>/', views.ReportComment.as_view(), name="report_comment"),
    path('create_article/', views.CreateArticle.as_view(), name="create_article"),
    path('article_edit/<slug:slug>/', views.EditArticle.as_view(), name='edit_article'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('endorse/<slug:slug>', views.ArticlesEndorsement.as_view(), name="articles_endorsement"),
    path('save/<slug:slug>', views.SavedArticle.as_view(), name="saved_article"),
]
