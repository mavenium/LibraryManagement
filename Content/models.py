from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=64,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=128,
        null=True,
        blank=True
    )
    surname = models.CharField(
        verbose_name=_('Surname'),
        max_length=128,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
        unique_together = ('first_name', 'last_name', 'surname')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
