from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    #path('recipes/', views.recipe_list, name='recipes'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_page, name='blog_page'),
    path('contact/', views.contact, name='contact'),
]