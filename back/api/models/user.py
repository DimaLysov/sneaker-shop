from django.db import models


class User(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    tg_username = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f"{self.tg_username}"

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural= 'Пользователи'