from rest_framework import serializers

from Content import models as ContentModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentModel.Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentModel.Publisher
        fields = '__all__'
