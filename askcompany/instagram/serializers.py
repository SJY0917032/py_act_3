from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
    # username,email 등등 을 임의로 만들수 있다.
    # username = serializers.ReadOnlyField(source='author.username')
    # author_email = serializers.ReadOnlyField(source='author.email')
    author = AuthorSerializer()
    
    class Meta:
        model = Post
        fields = [
            'pk',
            'author', # 중첩형으로 나올수 있다.
            'message',
            'create_at',
            'updated_at',
        ]