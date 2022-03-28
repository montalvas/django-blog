from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    template_name = 'blog/home.html'
    model = Post
    context_object_name = 'posts'
    
class BlogDetailView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post
    context_object_name = 'post'
