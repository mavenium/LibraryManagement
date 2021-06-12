from django.urls import path

from . import views

urlpatterns = [
    path('v1/authors/', views.AuthorList.as_view(), name="authors"),
]