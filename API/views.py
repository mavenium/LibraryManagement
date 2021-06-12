from django.shortcuts import get_list_or_404
from rest_framework import generics

from Content import models as ContentModels

from . import serializers


class AuthorList(generics.ListAPIView):
    """ Return a list of Author object """
    queryset = get_list_or_404(ContentModels.Author)
    serializer_class = serializers.AuthorSerializer


class PublisherList(generics.ListAPIView):
    """ Return a list of Publisher object """
    queryset = get_list_or_404(ContentModels.Publisher)
    serializer_class = serializers.PublisherSerializer


class BookByAuthorList(generics.ListAPIView):
    """ Return a list of Book object by Author object pk """
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        return ContentModels.Book.objects.filter(author__pk=self.kwargs['pk'])


class BookByPublisherList(generics.ListAPIView):
    """ Return a list of Book object by Publisher object pk """
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        return ContentModels.Book.objects.filter(publisher__pk=self.kwargs['pk'])


class BookCreate(generics.CreateAPIView):
    """ Create Book object """
    serializer_class = serializers.BookCreateSerializer
