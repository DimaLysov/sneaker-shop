from django.db import models


class Size(models.Model):
    size_rus = models.IntegerField()
    size_centimeters = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.size_rus}'

    class Meta:
        verbose_name = 'размер'
        verbose_name_plural= 'Размеры'
