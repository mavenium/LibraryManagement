from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, **extra_fields):
        user = self.model(**extra_fields)
        user.is_superuser = False
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user
