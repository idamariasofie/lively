from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib.auth.views import LoginView, LogoutView as AuthLogoutView
from django.contrib.auth import login as auth_login
from .models import Recipe, Comment, Profile
from .forms import CommentForm, ContactForm, SearchForm, ProfileForm

class CustomLogoutView(AuthLogoutView):
    template_name = 'registration/logout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class RecipeListView(generic.ListView):
    model = Recipe
    template_name = "blog/recipe_list.html"
    context_object_name = 'recipes'
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(status=1).order_by("-created_on")


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'blog/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.filter(approved=True).order_by("-created_on")
        return context


@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'blog/profile.html', {'form': form})


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        auth_login(self.request, self.object)
        messages.success(self.request, 'Account created successfully! You are now logged in.')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'Error in {field}: {error}')
        return response


class LoginView(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return response


@login_required
def delete_profile(request):
    if request.method == 'POST':
        try:
            # Delete user's profile
            request.user.profile.delete()

            # Delete the user
            request.user.delete()

            messages.success(request, 'Profile deleted successfully.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error deleting profile: {e}')

    return render(request, 'blog/delete_profile.html')


def home(request):
    recipes = Recipe.objects.filter(status=1).order_by("-created_on")
    return render(request, 'blog/home.html', {'recipes': recipes})


def blog_page(request):
    recipes = Recipe.objects.filter(status=1).order_by("-created_on")
    return render(request, 'blog/blog_page.html', {'recipes': recipes})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

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
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = recipe.comments.all()
    comment_form = CommentForm(user=request.user)

    # Search functionality
    query = request.GET.get('q')
    if query:
        comments = comments.filter(
            Q(author__username__icontains=query) |
            Q(content__icontains=query)
        )

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(user=request.user, data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment awaiting approval'
            )

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_form": comment_form,
            "query": query,
        },
    )


def add_comment(request, recipe_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.recipe_id = recipe_id
                comment.save()
                messages.success(request, 'Your comment was added successfully.')
                return redirect('recipe_detail', slug=comment.recipe.slug)
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'Error in {field}: {error}')
        else:
            messages.error(request, 'You must be logged in to add a comment.')
            return redirect('login')

    return redirect('recipe_detail', slug=recipe_id)
