from django.urls import path
from .views import PostList, DetailView, about, blog_page, contact, recipe_detail, categories, login

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('categories/', views.categories, name='categories'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('about/', about, name='about'),
    path('blog/', blog_page, name='blog'),
    path('contact/', contact, name='contact'),
    path('login/', contact, name='login'),
]