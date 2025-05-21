from django.db import models

from api.models import Size, ModelSneaker


class SKU(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    model_sneaker = models.ForeignKey(ModelSneaker, on_delete=models.CASCADE, default='None')
    price = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return f'{self.model_sneaker} - размер: {self.size}'

    class Meta:
        verbose_name = 'кроссовок'
        verbose_name_plural= 'Кроссовки'