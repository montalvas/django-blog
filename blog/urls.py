from django.urls import path
from . import views

from rest_framework.routers import SimpleRouter
from .views import PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)


app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    # CRUD
    path('post/new/', views.BlogCreateView.as_view(), name='post-new'),
    path('post/detail/<slug:slug>/', views.BlogDetailView.as_view(), name='post-detail'),
    path('post/update/<slug:slug>/', views.BlogUpdateView.as_view(), name='post-update'),
    path('post/delete/<slug:slug>/', views.BlogDeleteView.as_view(), name='post-delete'),
]
