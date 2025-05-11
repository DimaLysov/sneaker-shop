from django.db import models
from django.utils import timezone

from api.models import User


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый заказ'),
        ('processing', 'Ждем оплату'),
        ('paid', 'Оплачен'),
        ('sent', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    fullname = models.CharField(max_length=150)
    phone_number = models.BigIntegerField()
    delivery_address = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"{self.user} - {self.date}"

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
