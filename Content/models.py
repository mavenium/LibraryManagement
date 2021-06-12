from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=64,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=128,
        null=False,
        blank=False
    )
    surname = models.CharField(
        verbose_name=_('Surname'),
        max_length=128,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
        unique_together = ('first_name', 'last_name', 'surname')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=128,
        unique=True,
        null=False,
        blank=False
    )
    address = models.TextField(
        verbose_name=_('Address'),
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        help_text=_('Start the province code, like 02100000000'),
        max_length=11,
        null=False,
        blank=False,
        validators=[RegexValidator(
            regex=r'^0[0-9]{2,}[0-9]{7,}$',
            message=_('Please enter a valid phone number.'),
        )],
    )

    class Meta:
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=128,
        null=False,
        blank=False
    )
    number_of_pages = models.PositiveSmallIntegerField(
        verbose_name=_('Number Of Pages'),
        default=0,
        null=False,
        blank=False
    )
    year_of_publication = models.DateField(
        verbose_name=_('Year of publication'),
        null=False,
        blank=False
    )
    author = models.ManyToManyField(
        Author,
        verbose_name=_('Author'),
        related_name='book_author'
    )
    publisher = models.ManyToManyField(
        Publisher,
        verbose_name=_('Publisher'),
        related_name='book_publisher'
    )

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title

    def display_author(self):
        return ', '.join([author.get_full_name for author in self.author.all()])

    def display_publisher(self):
        return ', '.join([publisher.name for publisher in self.publisher.all()])
