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
