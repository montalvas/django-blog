from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField('Título', max_length=250)
    slug = models.SlugField('Slug', max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    content = models.TextField('Conteúdo')
    published = models.DateTimeField('Publicado', default=timezone.now)
    created = models.DateTimeField('Criado', auto_now_add=True)
    updated = models.DateField('atualizado', auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')
    
    class Meta:
        ordering = ('published',)
        # ordenação decrescente pela data de publicação
    
    def __str__(self):
        return self.title