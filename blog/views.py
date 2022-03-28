from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
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
    
class BlogCreateView(CreateView):
    template_name = 'blog/post-new.html'
    model = Post
    fields = ['title', 'content']
    success_url = 'blog:home'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
class BlogUpdateView(UpdateView):
    template_name = 'blog/post-update.html'
    model = Post
    fields = ['title', 'content']
    success_url = 'blog:home'
    
class BlogDeleteView(DeleteView):
    model = Post
