from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm

class PostList(generic.ListView):
    model = Recipe
    template_name = "blog/home.html"
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.all().order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f"Number of recipes: {self.get_queryset().count()}")
        return context

class DetailView(generic.DetailView):
    model = Recipe
    template_name = "blog/recipe_detail.html"

def categories(request):
    return render(request, 'blog/categories.html')

def about(request):
    return render(request, 'blog/about.html')

def blog_page(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/blog.html', {'recipes': recipes})

def contact(request):
    return render(request, 'blog/contact.html')

def recipe_detail(request, slug=None):
    post = get_object_or_404(Recipe, slug=slug)
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

