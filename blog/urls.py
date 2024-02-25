from django.urls import path
from .views import PostList, DetailView, about, blog_page, contact, recipe_detail

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('recipe/<slug:slug>/', recipe_detail, name='recipe_detail'),
    path('about/', about, name='about'),
    path('blog/', blog_page, name='blog'),
    path('contact/', contact, name='contact'),
]