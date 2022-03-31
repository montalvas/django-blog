from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

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
    slug = models.SlugField('Slug', max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    content = models.TextField('Conteúdo')
    published = models.DateTimeField('Publicado', default=timezone.now)
    created = models.DateTimeField('Criado', auto_now_add=True)
    updated = models.DateField('atualizado', auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')
    
    objects = models.Manager()
    get_published = PublishedManager()
    
    class Meta:
        ordering = ('-published',)
        # ordenação decrescente pela data de publicação
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])



def post_pre_save(signal, instance, sender, **kwargs):
    instance.slug = f'{instance.pk}-' + slugify(instance.title)

signals.pre_save.connect(post_pre_save, sender=Post)
    
    