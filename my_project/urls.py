from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include("blog.urls"), name='about'),
    path('home/', index_views.index, name='index'),
    path('recipes/', include("blog.urls"), name='recipes'),
    path('blog/', include("blog.urls"), name="blog-urls"),
    path('contact/', include("blog.urls"), name='contact'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
]
