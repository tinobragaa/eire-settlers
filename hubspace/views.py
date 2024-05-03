from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Articles, Profile, Comment
from .forms import CommentForm, ProfileForm, ArticleForm


class ArticlesList(generic.ListView):
    """
    View that displays the existent articles.
    """
    model = Articles
    queryset = Articles.objects.order_by("-created_on")
    paginate_by = 6

    def get_template_names(self):
        if self.request.path == '/articles/':
            return ['articles_list.html']
        else:
            return ['index.html']


class ArticleDetail(View):
    """
    View that displays the articles details.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Articles.objects.order_by("-created_on")
        articles = get_object_or_404(queryset, slug=slug)
        comments = (
            articles.comments.order_by("-created_on"))
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
        queryset = Articles.objects.order_by("-created_on")
        articles = get_object_or_404(queryset, slug=slug)
        comments = (
            articles.comments.order_by("-created_on"))
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


class CreateArticle(View):
    """
    A view that allow members to create a new article.
    """
    def get(self, request):
        if self.request.user.is_authenticated:
            form = ArticleForm()
            context = {"form": form, }

            return render(request, "create_article.html", context)
        else:

            return redirect("index.html")

    def post(self, request, *arg, **kwargs):
        if self.request.user.is_authenticated:
            form = ArticleForm(request.POST)
            if form.is_valid():
                form.instance.member = self.request.user
                form.instance.slug = slugify(form.instance.title)
                if 'image_preview' in request.FILES:
                    form.instance.image_preview = request.FILES[
                        'image_preview'
                        ]
                new_article = form.save()
                messages.success(request, 'Article created successfully!')

                return redirect("article_detail", new_article.slug)
            else:

                return render(request, "create_article.html", {"form": form})
        else:

            return redirect("index.html")


class EditArticle(View):
    """
    View that allow members to edit their articles.
    """
    def get(self, request, *arg, **kwargs):
        if "slug" in self.kwargs:
            article = get_object_or_404(
                Articles, slug=self.kwargs["slug"])

            if (self.request.user == article.member or request.user.is_staff):

                form = ArticleForm(instance=article)

                context = {"form": form, }

                return render(request, "edit_article.html", context)
            else:

                return redirect("index.html")

    def post(self, request, *arg, **kwargs):
        article = get_object_or_404(
            Articles, slug=self.kwargs["slug"])
        if (self.request.user == article.member or request.user.is_staff):
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                if 'image_preview' in request.FILES:
                    form.instance.image_preview = request.FILES[
                        'image_preview'
                        ]
                edited_article = form.save()
                messages.success(request, 'Article updated successfully!')

                return redirect("article_detail", edited_article.slug)


class DeleteArticle(View):
    """
    View that allow members to delete their articles.
    """
    def get(self, request, slug, *arg, **kwargs):
        article = get_object_or_404(
            Articles, slug=self.kwargs["slug"])

        context = {"article": article}

        if (self.request.user == article.member or request.user.is_staff):
            return render(request, "delete_article.html", context)

        else:
            return redirect("index.html")

    def post(self, request, *arg, **kwargs):
        article = get_object_or_404(
            Articles, slug=self.kwargs["slug"])

        if (self.request.user == article.member or request.user.is_staff):
            article.delete()
            return HttpResponseRedirect(reverse('home'))

        else:

            return redirect("index.html")


class ArticlesEndorsement(View):
    """
    View that enables the article to be liked by other members.
    """
    def post(self, request, slug):
        articles = get_object_or_404(Articles, slug=slug)
        if articles.endorsement.filter(id=request.user.id).exists():
            articles.endorsement.remove(request.user)
        else:
            articles.endorsement.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


class SavedArticle(View):
    """
    View that enables the article to be saved by members.
    """
    def post(self, request, slug):
        articles = get_object_or_404(Articles, slug=slug)
        if articles.saved_items.filter(id=request.user.id).exists():
            articles.saved_items.remove(request.user)
        else:
            articles.saved_items.add(request.user)
            messages.success(request, 'Successfully saved!')

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


class SavedArticles(View):
    """
    View that displays all articles saved by the member logged in.
    """
    template_name = "saved_articles.html"

    def get(self, request, user):
        user_object = get_object_or_404(User, username=user)
        articles = Articles.objects.filter(saved_items=user_object)
        return render(
            request,
            self.template_name,
            {'articles_list': articles, 'user': user_object}
        )


class MemberArticles(View):
    """
    View that displays the articles created by the member logged in.
    """
    template_name = "member_articles.html"

    def get(self, request, user):
        user_object = get_object_or_404(User, username=user)
        articles = Articles.objects.filter(member=user_object)
        return render(
            request,
            self.template_name,
            {'articles_list': articles, 'user': user_object}
        )


class MemberProfile(View):
    """
    View that displays the profile page.
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
            "first_name": profile_detail.first_name,
            "last_name": profile_detail.last_name,
            "profile": profile_detail,
            "pronouns": profile_detail.pronouns,
            "image": profile_detail.image,
            "location": profile_detail.location,
            "nationality": profile_detail.nationality,
            "about": profile_detail.about
            }

        return render(request, "member_profile.html", context)


@login_required(login_url='/accounts/login/')
def update_profile(request):
    """
    View that will update the member profile.
    """
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('member_profile')

    context = {'form': form}
    return render(request, "edit_profile.html", context)


@login_required(login_url='/accounts/login/')
def delete_profile(request):
    """
    View that will delete the member profile.
    """
    if request.method == "POST":
        user = request.user
        if user.is_staff or user == request.user:
            user.delete()
            logout(request)
            messages.warning(request, 'Profile was deleted!')
            return redirect('/')

    return render(request, "delete_profile.html")


@login_required(login_url='/accounts/login/')
def edit_comment(request, comment_id):
    """
    View that allows members to edit their comments.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.member or request.user.is_staff:
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(
                    request,
                    'The comment was edited successfully!'
                )
                return HttpResponseRedirect(reverse(
                    'article_detail', args=[comment.article.slug]
                ))
        else:
            form = CommentForm(instance=comment)

        context = {'form': form}
        return render(request, "edit_comment.html", context)
    else:
        return HttpResponseNotFound('Permission Denied')


@login_required(login_url='/accounts/login/')
def delete_comment(request, comment_id):
    """
    View that allows members to delete their comments.
    """
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.member or request.user.is_staff:
            comment.delete()
            messages.success(request, 'The comment was deleted successfully!')
            return HttpResponseRedirect(reverse(
                'article_detail', args=[comment.article.slug]
            ))
        else:
            return HttpResponseNotFound('Permission Denied')

    return render(request, "delete_comment.html")


class ReportComment(View):
    """
    View that enables comments to be reported/unreported.
    """
    def post(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, id=pk)

        if not comment.reported:
            comment.reported = True
            comment.save()
            messages.success(request, 'Comment reported.')
        elif comment.reported and self.request.user.is_superuser:
            comment.reported = False
            comment.save()
            messages.success(request, 'Comment unreported.')
        else:
            messages.success(request, 'Comment reported.')

        article_url = reverse(
            'article_detail', kwargs={'slug': comment.article.slug}
            )
        return HttpResponseRedirect(article_url)
