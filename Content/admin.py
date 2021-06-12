from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'surname'
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


class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone_number'
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