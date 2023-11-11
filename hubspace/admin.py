from django.contrib import admin
from .models import Articles, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Articles)
class ArticlesAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('created_on',)
    list_display = ('body', 'article', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Profile)
