from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from recipes import views as recipes_views
from contact import views as contact_views
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include("blog.urls"), name='about'),
    path('home/', index_views.index, name='index'),
    path('recipes/', recipes_views.recipes_lively, name='recipes'),
    path("", include("blog.urls"), name="blog-urls"),
    # Remove the extra comma from the line below
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
]
