from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=100,
                             required=True,
                             help_text='Obrigatório. E-mail de cadastro.')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        e = self.cleaned_data['email']
        
        if User.objects.filter(email=e).exists():
            raise ValidationError('O e-mail já está cadastrado.')