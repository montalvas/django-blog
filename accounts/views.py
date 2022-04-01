from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Signup
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse_lazy

# Create your views here. 
class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_message = "Olá, seja bem-vindo!"
    
class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Desconectado com sucesso.")
        return super().dispatch(request, *args, **kwargs)
    
class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserForm
    success_url = reverse_lazy('accounts:login')
    success_message = "Usuário criado com sucesso."
    