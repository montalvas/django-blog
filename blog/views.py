from django.views.generic import ListView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    template_name = 'blog/home.html'
    model = Post
    context_object_name = 'posts'
