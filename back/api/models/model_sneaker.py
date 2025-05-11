from django.db import models

from api.models import Brand


class ModelSneaker(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models', default='No brand')
    name = models.CharField(max_length=100, default='No name')
    color = models.CharField(max_length=100, default='No color')
    image_url = models.ImageField(upload_to='api/images', default="api/images/img.png")

    def __str__(self):
        return f"{self.brand} '{self.name}' {self.color}"

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'Модели кроссовок'
