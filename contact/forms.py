from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=255, widget=forms.TextInput(attrs={'placeholder':'Digite seu nome'}), required=True)
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder':'Digite seu e-mail'}), required=True)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'placeholder':'Digite o assunto'}), required=True)