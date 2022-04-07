from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    send = False
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email = EmailMessage(
            "Mensagem do Blog Django",
            f"De {name} <{email}> Escreveu:\n\n{message}",
            "no-reply@inbox.mailtrap.io",
            ["admin@django.blog"],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
        except:
            send = False
        
    context = {
        'form': form,
        'success': send
    }
    
    return render(request, 'contact/contact.html', context)
    