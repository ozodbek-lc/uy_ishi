from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class KunAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="authors/")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"


class KunPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(KunAuthor, on_delete=models.CASCADE, related_name="posts")

    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="Kun uz/")
    tags = models.CharField(max_length=255)

    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
