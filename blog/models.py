from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

# IMAGES
from django.utils.html import mark_safe

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')
    
class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    created = models.DateTimeField('Criado', auto_now_add=True)
    updated = models.DateField('atualizado', auto_now=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']
    
    def __str__(self):
        return self.name
    
def get_default_category():
    return Category.objects.get_or_create(name='Geral')[0]

class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField('Título', max_length=250)
    slug = models.SlugField('Slug', max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    content = RichTextField()
    category = models.ManyToManyField(Category, default=get_default_category, related_name='get_posts')
    image = models.ImageField(upload_to='blog', null=True, blank=True)
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
    
    