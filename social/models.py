from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField('Identificação', max_length=100, unique=True)
    description = models.CharField('Descrição', max_length=100)
    url = models.URLField(max_length=200, null=False, blank=False)
    created = models.DateTimeField('Criado', auto_now_add=True)
    updated = models.DateField('atualizado', auto_now=True)
    
    class Meta:
        ordering = ['key']
        
    def __str__(self):
        return self.key