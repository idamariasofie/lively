from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm

def home(request):
    recipes = Recipe.objects.all()

    # For debugging purposes, print the number of recipes
    print(f"Number of recipes: {recipes.count()}")

    return render(request, 'blog/home.html', {'recipe_detail': recipes})

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

class DetailView(generic.DetailView):
    model = Recipe
    template_name = "blog/recipe_detail.html"

def recipe_detail(request):
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/recipe_detail.html'
    post = queryset.first() 
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

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