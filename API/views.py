from django.shortcuts import get_list_or_404
from rest_framework import generics

from Content import models as ContentModels

from . import serializers


class AuthorList(generics.ListAPIView):
    queryset = get_list_or_404(ContentModels.Author)
    serializer_class = serializers.AuthorSerializer


class PublisherList(generics.ListAPIView):
    queryset = get_list_or_404(ContentModels.Publisher)
    serializer_class = serializers.PublisherSerializer


class BookByAuthorList(generics.ListAPIView):
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        return ContentModels.Book.objects.filter(author__pk=self.kwargs['pk'])


class BookByPublisherList(generics.ListAPIView):
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        return ContentModels.Book.objects.filter(publisher__pk=self.kwargs['pk'])

