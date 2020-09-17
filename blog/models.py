from datetime import datetime

from django.db import models
from django.urls import reverse

from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_tag", args=[self.name])


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    published = models.BooleanField(default=False)
    img = models.ImageField(blank=True, upload_to="post_images")
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="post_tag")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.old_published = self.published

    def save(self, *args, **kwargs):
        if self.published and self.old_published != self.published:
            self.pub_date = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
