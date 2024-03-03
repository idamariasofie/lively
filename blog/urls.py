from django.urls import path
from .views import (
    home,
    RecipeListView,
    RecipeDetailView,
    about,
    blog_page,
    contact,
    add_comment,
    search_results,
    profile,
    delete_profile,
    recipe_detail,
)

urlpatterns = [
    path('', home, name='home'),
    path('recipes/<slug:slug>/recipe_detail/', recipe_detail, name='recipe_detail'),
    path('about/', about, name='about'),
    path('blog/', blog_page, name='blog'),
    path('contact/', contact, name='contact'),
    path('recipes/<slug:slug>/add_comment/', add_comment, name='add_comment'),
    path('search/', search_results, name='search_results'),
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]
