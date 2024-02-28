from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string 
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from .models import Recipe, Comment
from .forms import CommentForm, ContactForm, SearchForm


class PostList(generic.ListView):
    model = Recipe
    template_name = "blog/home.html"
    context_object_name = 'recipes'
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.all().order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all().order_by("-created_on")
        return context

class DetailView(generic.DetailView):
    model = Recipe
    template_name = "blog/recipe_detail.html"

def categories(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def blog_page(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/blog_page.html', {'recipes': recipes})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Simulate saving the form data or performing any other actions
            # Instead of sending an email, you can print or log the data
            print("Simulating contact form submission...\n")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Subject: {subject}")
            print(f"Message: {message}")

            return render(request, 'blog/contact_success.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})

def recipe_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Search functionality
    query = request.GET.get('q')
    if query:
        comments = comments.filter(
            Q(author__username__icontains=query) |
            Q(content__icontains=query)
        )

    if request.method == "POST" and request.user.is_authenticated:
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
            "query": query,
        },
    )

def add_comment(request, slug=None):
    post = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
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

    return redirect('recipe_detail', slug=slug)

def search_results(request):
    query = request.GET.get('search_query', '')
    results = Recipe.objects.filter(title__icontains=query)
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})
