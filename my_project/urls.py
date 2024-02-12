from django.contrib import admin
from django.urls import path, include
from hello_world import views as index_views
from about import views as about_views

urlpatterns = [
    path('hello/', index_views.index, name='index'),
    path('about/', about_views.about_lively, name='about'),
    path('admin/', admin.site.urls),
]