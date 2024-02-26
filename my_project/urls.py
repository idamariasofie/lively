from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from blog.views import PostList, DetailView, about, blog_page, contact, recipe_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('recipes/', PostList.as_view(), name='recipes'),  # Use PostList as the view function for recipes
    path('blog/', blog_page, name='blog_page'),
    path('contact/', contact, name='contact'),
    path('recipes/<slug:slug>/', DetailView.as_view(), name='recipe_detail'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
]
