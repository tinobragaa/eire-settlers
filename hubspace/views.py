from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Articles, Profile
from .forms import CommentForm
from django.contrib.auth.models import User


class ArticlesList(generic.ListView):
    model = Articles
    queryset = Articles.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Articles.objects.filter(status=1)
        articles = get_object_or_404(queryset, slug=slug)
        comments = (
            articles.comments.filter(approved=True).order_by("-created_on"))
        endorsed = False
        saved = False
        if articles.endorsement.filter(id=self.request.user.id).exists():
            endorsed = True
        if articles.saved_items.filter(id=self.request.user.id).exists():
            saved = True

        return render(
            request,
            "article_detail.html",
            {
                "articles": articles,
                "comments": comments,
                "commented": False,
                "endorsed": endorsed,
                "saved": saved,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Articles.objects.filter(status=1)
        articles = get_object_or_404(queryset, slug=slug)
        comments = (
            articles.comments.filter(approved=True).order_by("-created_on"))
        endorsed = False
        saved = False
        if articles.endorsement.filter(id=self.request.user.id).exists():
            endorsed = True
        if articles.saved_items.filter(id=self.request.user.id).exists():
            saved = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = articles
            comment.member = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "article_detail.html",
            {
                "articles": articles,
                "comments": comments,
                "commented": True,
                "endorsed": endorsed,
                "saved": saved,
                "comment_form": CommentForm()
            },
        )


class ArticlesEndorsement(View):

    def post(self, request, slug):
        articles = get_object_or_404(Articles, slug=slug)

        if articles.endorsement.filter(id=request.user.id).exists():
            articles.endorsement.remove(request.user)
        else:
            articles.endorsement.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


class SavedArticle(View):

    def post(self, request, slug):
        articles = get_object_or_404(Articles, slug=slug)

        if articles.saved_items.filter(id=request.user.id).exists():
            articles.saved_items.remove(request.user)
        else:
            articles.saved_items.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


class MemberProfile(View):
    """
    View for profile page.
    """
    def get(self, request, *arg, **kwargs):
        if "user" in self.kwargs:
            member_info = get_object_or_404(
                User, username=self.kwargs["user"])
            profile_detail = get_object_or_404(
                Profile, user=member_info.id)
        else:
            member_info = get_object_or_404(
                User, username=request.user.username)
            profile_detail = get_object_or_404(
                Profile, user=request.user.id)

        context = {
            "user": member_info,
            "pronouns": profile_detail.pronouns,
            "image": profile_detail.image,
            "location": profile_detail.location,
            "nationality": profile_detail.nationality,
            "about": profile_detail.about
            }

        return render(request, "member_profile.html", context)
