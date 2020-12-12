from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free.
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a `User` with an email and password."""

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.is_activate = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):

        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, ):
    username = models.CharField(max_length=16, unique=True, blank=True, null=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    mobile = models.CharField(max_length=15, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email

    def get_short_name(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
