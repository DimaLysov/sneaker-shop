from django.contrib import admin
from django.apps import apps
from django.utils.html import mark_safe

from .filters.sku import BrandFilter, ModelSneakerFilter
from .models import SKU, ModelSneaker, Size, CartItem


class SKUAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'sneaker_name', 'color', 'size', 'price', 'count')
    list_filter = ('model_sneaker__brand', 'model_sneaker__name', 'size')
    # list_filter = (BrandFilter, ModelSneakerFilter, 'size')

    def brand_name(self, obj):
        return obj.model_sneaker.brand.name

    brand_name.short_description = "Бренд"

    def sneaker_name(self, obj):
        return obj.model_sneaker.name

    sneaker_name.short_description = "Имя модели"

    def color(self, obj):
        return obj.model_sneaker.color



class ModelSneakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'name', 'color', 'image_tag')
    list_filter = ('brand',)
    search_fields = ('name',)

    def image_tag(self, obj):
        if obj.image_url:  # Если изображение существует
            return mark_safe(f'<img src="{obj.image_url.url}" style="width: 100px; height: 100px;" />')
        return "Нет изображения"

    image_tag.short_description = "Фото"


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size_centimeters', 'size_rus',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sku', 'quantity')


admin.site.register(SKU, SKUAdmin)
admin.site.register(ModelSneaker, ModelSneakerAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(CartItem, CartItemAdmin)

# Получаем все модели из приложения my_app
app_models = apps.get_app_config('api').get_models()

for model in app_models:
    try:
        admin.site.register(model)  # Регистрируем модель с дефолтными настройками
    except admin.sites.AlreadyRegistered:  # На случай, если модель уже зарегистрирована
        pass
