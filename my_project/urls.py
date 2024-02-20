from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from recipes import views as recipes_views
from about import views as about_views
from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_views.about_lively, name='about'),
    path('home/', index_views.index, name='index'),
    path('recipes/', recipes_views.recipes_lively, name='recipes'),
    path("", include("blog.urls"), name="blog-urls"),
    path('contact/', contact_views.contact_lively, name='contact'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
]