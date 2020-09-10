from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __repr__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('full_news', kwargs={'pk': self.pk})