from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# MESSAGES
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# USER
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

admin = User.objects.get(id=1)

# Create your views here.
class BlogListView(ListView):
    template_name = 'blog/home.html'
    model = Post
    context_object_name = 'posts'
    
class BlogDetailView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post
    context_object_name = 'post'
    
class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'blog/post-new.html'
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')
    success_message = "%(field)s criado."
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title
        )
    
    def form_valid(self, form):
        form.instance.author = admin  #self.request.user
        
        return super().form_valid(form)
    
class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'blog/post-update.html'
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')
    success_message = "%(field)s alterado com sucesso."
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title
        )
    
class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'blog/post-delete.html'
    model = Post
    success_url = reverse_lazy('blog:home')
    success_message = "Deletado com sucesso"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)