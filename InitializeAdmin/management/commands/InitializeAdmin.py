from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Create default superuser """
    admin_username = 'admin'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username=self.admin_username).exists():
            User.objects.create_superuser(
                password='admin@123',
                username=self.admin_username,
                email='admin@test.com'
            )
        else:
            print('An admin user with username={} exists'.format(self.admin_username))
