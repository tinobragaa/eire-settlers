from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Articles


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
                "endorsed": endorsed
            },
        )
