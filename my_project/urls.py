from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  
    path('about/', blog_views.about, name='about'),
    path('home/', index_views.index, name='index'),
    path('recipes/<slug:slug>/', blog_views.recipe_detail, name='recipe_detail'),
    path('blog/', blog_views.blog_page, name="blog-urls"),
    path('contact/', blog_views.contact, name='contact'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
]