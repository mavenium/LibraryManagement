from django.urls import path

from . import views

urlpatterns = [
    path('v1/authors/', views.AuthorList.as_view(), name="authors"),
    path('v1/publishers/', views.PublisherList.as_view(), name="publishers"),
    path('v1/books_by_author/<int:pk>/', views.BookByAuthorList.as_view(), name="books_by_author"),
    path('v1/books_by_publisher/<int:pk>/', views.BookByPublisherList.as_view(), name="books_by_publisher"),
    path('v1/books_create/', views.BookCreate.as_view(), name="books_create"),
]