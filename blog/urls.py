from django.urls import path
from .views import (
    home,
    RecipeListView,
    RecipeDetailView,
    about,
    blog_page,
    contact,
    add_comment,
    profile,
    delete_profile,
    recipe_detail,
)

urlpatterns = [
    path('', home, name='home'),  
    path('recipes/<slug:slug>/recipe_detail/', recipe_detail, name='recipe_detail'),
    path('about/', about, name='about'),
    path('blog/', blog_page, name='blog_page'),  
    path('contact/', contact, name='contact'),
    path('recipes/<slug:slug>/add_comment/', add_comment, name='add_comment'),
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
    path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
]
