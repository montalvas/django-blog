from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')

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
    
    objects = models.Manager()
    get_published = PublishedManager()
    
    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.pk])
    
    class Meta:
        ordering = ('-published',)
        # ordenação decrescente pela data de publicação
    
    def __str__(self):
        return self.title
    
    