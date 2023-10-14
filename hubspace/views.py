from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from .models import Articles, Profile, Comment
from .forms import CommentForm, ProfileForm
from django.contrib.auth.models import User


class ArticlesList(generic.ListView):
    """
    View that displays all articles on the landing page.
    """
    model = Articles
    queryset = Articles.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class ArticleDetail(View):
    """
    View that displays the article details.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Articles.objects.filter(status=1)
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
        queryset = Articles.objects.filter(status=1)
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


class ArticlesEndorsement(View):
    """
    View that enables the post to be liked by members.
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
    View that enables the post to be saved by members.
    """
    def post(self, request, slug):
        articles = get_object_or_404(Articles, slug=slug)

        if articles.saved_items.filter(id=request.user.id).exists():
            articles.saved_items.remove(request.user)
        else:
            articles.saved_items.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


class MemberProfile(View):
    """
    View to display the profile page.
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
    View that will update the user profile.
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
    View that will delete the user profile.
    """
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.warning(request, 'Profile was deleted!')
        return redirect('/')

    return render(request, "delete_profile.html")


@login_required(login_url='/accounts/login/')
def edit_comment(request, comment_id):
    """
    View that allow to edit a comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'The comment was edited successfully!')
            return HttpResponseRedirect(reverse(
                'article_detail', args=[comment.article.slug]))
    else:
        form = CommentForm(instance=comment)

    context = {'form': form}
    return render(request, "edit_comment.html", context)


@login_required(login_url='/accounts/login/')
def delete_comment(request, comment_id):
    """
    View that allow users to delete their comments.
    """
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        messages.success(request, 'The comment was deleted successfully!')
        return HttpResponseRedirect(reverse(
            'article_detail', args=[comment.article.slug]))

    return render(request, "delete_comment.html")
