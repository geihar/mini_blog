from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

from PIL import Image


class User(AbstractUser):
    is_staff = models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        super(User, self).save(*args, **kwargs)

        if not self.username == 'admin':
            self.user_permissions.add(22)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default="1.jpg", upload_to="user_images")

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.img.path)
        if img.height > 128 or img.width > 128:
            output_size = (128, 128)
            img.thumbnail(output_size)
            img.save(self.img.path)
