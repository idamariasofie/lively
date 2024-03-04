from django.urls import path
from django.contrib.auth import views as auth_views
from allauth.account.views import SignupView
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
    CustomLogoutView,
    search_results
)

urlpatterns = [
    path('', home, name='home'),  
    path('about/', about, name='about'),
    path('blog/', blog_page, name='blog_page'),  
    path('contact/', contact, name='contact'),
    path('add_comment/<slug:slug>/', add_comment, name='add_comment'),
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
    path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('search_results/', search_results, name='search_results'),
]
