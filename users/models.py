from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class User(AbstractUser):
    is_staff = models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        super(User, self).save(*args, **kwargs)

        if not self.username == 'admin':
            self.user_permissions.add(22)


