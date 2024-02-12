from django.contrib import admin
from django.urls import path, include
from hello_world import views as index_views
from recipes import views as recipes_views
from about import views as about_views
from contact import views as contact_views

urlpatterns = [
    path('hello/', index_views.index, name='index'),
    path('recipes/', recipes_views.recipes_lively, name='recipes'),
    path('about/', about_views.about_lively, name='about'),
    path('contact/', contact_views.contact_lively, name='contact'),
    path('admin/', admin.site.urls),
]