from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here. 
class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_message = "Olá, seja bem-vindo!"
    
class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Desconectado com sucesso.")
        return super().dispatch(request, *args, **kwargs)
    