from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Articles
from .forms import CommentForm


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
        if articles.endorsement.filter(id=self.request.user.id).exists():
            endorsed = True

        return render(
            request,
            "article_detail.html",
            {
                "articles": articles,
                "comments": comments,
                "commented": False,
                "endorsed": endorsed,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Articles.objects.filter(status=1)
        articles = get_object_or_404(queryset, slug=slug)
        comments = (
            articles.comments.filter(approved=True).order_by("-created_on"))
        endorsed = False
        if articles.endorsement.filter(id=self.request.user.id).exists():
            endorsed = True

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
