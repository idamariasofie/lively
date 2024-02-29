from django.contrib import admin
from django.urls import path, include
from home import views as index_views
from blog.views import RecipeListView, RecipeDetailView, about, blog_page, contact, add_comment, search_results, home, profile, delete_profile

urlpatterns = [
    path('about/', about, name='about'),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('', home, name='home'),  
    path('contact/', contact, name='contact'),
    path('search_results/', search_results, name='search_results'),
    path('summernote/', include('django_summernote.urls')),

    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<slug:slug>/add_comment/', add_comment, name='add_comment'),
    path('blog/', include('blog.urls')), 
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]
