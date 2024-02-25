from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from blog.views import PostList, DetailView, about, blog_page, contact  # Import the 'about' view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostList.as_view(), name='home'),
    path('about/', about, name='about'),  # Use the correct 'about' view
    path('blog/', blog_page, name='blog_page'),
    path('contact/', contact, name='contact'),  # Assuming 'contact' is defined in 'blog.views'
    path('recipes/<slug:slug>/', DetailView.as_view(), name='recipe_detail'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
]
