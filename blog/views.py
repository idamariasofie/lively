from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm

def home(request):
    return render(request, 'blog/home.html')

def recipe_list(request):
    return render(request, 'blog/recipe_list.html')  # Renamed from 'recipes' to 'recipe_list'

def about(request):
    return render(request, 'blog/about.html')

def blog_page(request):
    return render(request, 'blog/blog_page.html')

def contact(request):
    return render(request, 'blog/contact.html')

class PostList(generic.ListView):
    queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "blog/home.html"
    paginate_by = 6

def recipe_detail(request, slug):
    """
    Display an individual :model:`blog.Recipe`.

    Args:
        slug (str): The slug of the recipe.

    Returns:
        HttpResponse: Rendered HTML response.

    Context:
        post (Recipe): An instance of :model:`blog.Recipe`.
        comments (QuerySet): Comments related to the recipe.
        comment_count (int): Count of approved comments.
        comment_form (CommentForm): Form for submitting comments.

    Template:
        blog/recipe_detail.html
    """
    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comment.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment awaiting approval'
            )

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