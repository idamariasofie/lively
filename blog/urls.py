from django.urls import path
from .views import PostList, DetailView, about, blog_page, contact, recipe_detail

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('blog/', blog_page, name='blog_page'),
    path('contact/', contact, name='contact'),
    path('recipes/<slug:slug>/', DetailView.as_view(), name='recipe_detail'),
]
