from django.contrib import admin
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'surname',
        'get_book_count'
    ]
    list_display_links = [
        'first_name'
    ]
    search_fields = [
        'first_name',
        'last_name',
        'surname'
    ]
    actions = [
        'delete_selected'
    ]
    ordering = [
        '-pk'
    ]
    list_filter = [
        'first_name',
        'last_name',
        'surname'
    ]

    def get_book_count(self, obj):
        return obj.book_count

    def get_queryset(self, request):
        return self.model.objects.annotate(book_count=Count('book_author'))

    get_book_count.short_description = _('Book Count')


class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone_number',
        'get_book_count'
    ]
    list_display_links = [
        'name'
    ]
    search_fields = [
        'name',
        'phone_number'
    ]
    actions = [
        'delete_selected'
    ]
    ordering = [
        '-pk'
    ]
    list_filter = [
        'name'
    ]

    def get_book_count(self, obj):
        return obj.book_count

    def get_queryset(self, request):
        return self.model.objects.annotate(book_count=Count('book_publisher'))

    get_book_count.short_description = _('Book Count')


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'number_of_pages',
        'year_of_publication',
        'display_author',
        'display_publisher'
    ]
    list_display_links = [
        'title'
    ]
    search_fields = [
        'title'
    ]
    actions = [
        'delete_selected'
    ]
    ordering = [
        '-pk'
    ]
    list_filter = [
        'year_of_publication',
        'author',
        'publisher'
    ]

    models.Book.display_author.short_description = _('Author')
    models.Book.display_publisher.short_description = _('Publisher')


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Book, BookAdmin)