from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models

from . import managers

from extensions import choices


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=64,
        unique=True,
        null=False,
        blank=False
    )
    date_of_join = models.DateField(
        verbose_name=_('Date Of Join'),
        auto_now_add=True,
        null=False,
        blank=False
    )
    date_of_birth = models.DateField(
        verbose_name=_('Date Of Birthday'),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name=_('Is Active'),
        help_text=_('Active account in the system'),
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('Is Staff'),
        help_text=_('The user can access the system management section'),
        default=False
    )
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
    gender = models.PositiveSmallIntegerField(
        verbose_name=_('Gender'),
        choices=choices.GenderChoices.generate_choices(),
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        unique=True,
        blank=False,
        null=False
    )

    objects = managers.UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_gender_name(self):
        return next(filter(lambda t: t[0] == self.gender, choices.GenderChoices.generate_choices()), ("", ""))[1]
