from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostList.as_view(), name='recipe_detail'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_page, name='blog_page'),
    path('contact/', views.contact, name='contact'),
]