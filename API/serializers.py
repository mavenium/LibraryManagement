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


class BookSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = ContentModel.Book
        fields = [
            'title',
            'number_of_pages',
            'year_of_publication',
            'author',
            'publisher'
        ]
