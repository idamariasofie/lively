from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6

def recipe_detail(request, slug):
    """
    Display an individual :model:`blog.Recipe`.

    **Context**

    ``post``
        An instance of :model:`blog.Recipe`.

    **Template:**

    :template:`blog/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comment.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )