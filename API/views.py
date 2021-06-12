from django.shortcuts import get_list_or_404
from rest_framework import generics

from Content import models as ContentModels

from . import serializers


class AuthorList(generics.ListAPIView):
    queryset = get_list_or_404(ContentModels.Author)
    serializer_class = serializers.AuthorSerializer

