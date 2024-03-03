from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.views.generic.detail import DetailView
from .models import Recipe, Comment, Profile
from .forms import CommentForm, ContactForm, SearchForm, ProfileForm


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


@login_required
def delete_profile(request):
    if request.method == 'POST':
        try:
            request.user.profile.delete()
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
