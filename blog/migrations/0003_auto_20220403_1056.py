# Generated by Django 3.2.12 on 2022-04-03 13:56

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220328_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('updated', models.DateField(auto_now=True, verbose_name='atualizado')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default=blog.models.get_default_category, related_name='get_posts', to='blog.Category'),
        ),
    ]
