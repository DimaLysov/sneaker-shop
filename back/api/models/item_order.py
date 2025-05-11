from django.db import models

from api.models import SKU, Order


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.order} - {self.sku}, {self.quantity} шт, по {self.price}"

    class Meta:
        verbose_name = 'содержимое заказа'
        verbose_name_plural = 'Содержимое заказов'