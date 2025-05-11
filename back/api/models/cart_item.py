from django.db import models

from api.models import User, SKU


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user} - {self.sku} ({self.quantity})'

    class Meta:
        verbose_name = 'товар в корзину'
        verbose_name_plural= 'Корзины пользователей'