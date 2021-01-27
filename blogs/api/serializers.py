from rest_framework import serializers
from blogs.models import Blog
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'content', 'tags', 'featured', 'block', 'date_added', 'date_edited',
                  'owner']
        extra_kwargs = {
            'title': {
                'read_only': True,
                # 'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """
        create and return a new 'Snippet' instance, given the validated_data 
        """
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.content = validated_data.get('content', instance.content)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.featured = validated_data.get('featured', instance.featured)
        instance.block = validated_data.get('block', instance.block)
        instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.date_edited = validated_data.get('date_edited', instance.date_edited)
        instance.save()
        return instance


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']