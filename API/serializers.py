from rest_framework import serializers

from Content import models as ContentModel


class AuthorSerializer(serializers.ModelSerializer):
    """ Serializer for fetch Author object """
    class Meta:
        model = ContentModel.Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    """ Serializer for fetch Publisher object """
    class Meta:
        model = ContentModel.Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """ Serializer for fetch Book object """
    author = serializers.StringRelatedField(many=False)
    publisher = serializers.StringRelatedField(many=True)

    class Meta:
        model = ContentModel.Book
        fields = [
            'title',
            'number_of_pages',
            'year_of_publication',
            'author',
            'publisher',
            'pk'
        ]


class BookCreateSerializer(serializers.ModelSerializer):
    """ Serializer for create Book object """
    class Meta:
        model = ContentModel.Book
        fields = [
            'title',
            'number_of_pages',
            'year_of_publication',
            'author',
            'publisher'
        ]
