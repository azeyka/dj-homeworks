from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_subscription = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(verbose_name='Изображение')
    text = models.TextField(verbose_name='Текст статьи')
    paid = models.BooleanField(verbose_name='Платный контент', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
