from django.contrib import admin
from .models import Post, Category


# admin.site.register(Post) Outra forma de cadastrar
# não escolhe os campos a serem mostrados

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author',
                    'created', 'updated', 'status')
    
    list_filter = ('status', 'created', 'published', 'author')
    # Faz a filtragem dos resultados por atributo
    
    # raw_id_fields = ('author',)
    # Permite a seleção de mais de um objeto para o atributo
    # usado para many-to-one, many-to-many e foreign keys
    
    date_hierarchy = 'published'
    # Cria uma navegação detalhada baseada em data
    
    search_fields = ('title',)
    # pesquisa o objeto por atributo
    
    prepopulated_fields = {'slug': ('title',)}
    # cria o slug automaticamente utilizando o title como base
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')