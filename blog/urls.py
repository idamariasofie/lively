from django.urls import path
from .views import RecipeListView, RecipeDetailView, about, blog_page, contact, add_comment, search_results

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('categories/', categories, name='categories'),
    path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('about/', about, name='about'),
    path('blog/', blog_page, name='blog'),
    path('contact/', contact, name='contact'),
    path('recipes/<slug:slug>/add_comment/', add_comment, name='add_comment'),
    path('search/', search_results, name='search_results'),
]
