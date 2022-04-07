from rest_framework import serializers
from django.utils.html import strip_tags
from .models import Post

        
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'content',
            'category',
            'created',
        )
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['content'] = strip_tags(instance.content)
        return data