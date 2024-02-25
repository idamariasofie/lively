from .views import PostList, DetailView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_page, name='blog_page'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', DetailView.as_view(), name='recipe_detail'),
]