from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_detail, name='recipes'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_page, name='blog_page'),
    path('contact/', views.contact, name='contact'),
]