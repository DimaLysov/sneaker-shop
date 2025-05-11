from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class BrandFilter(admin.SimpleListFilter):
    title = _('Бренд')
    parameter_name = 'brand'  # Используем parameter_name без вложенных lookups

    def lookups(self, request, model_admin):
        from api.models import Brand  # Импортируем модель
        return [(brand.id, brand.name) for brand in Brand.objects.all()]

    def queryset(self, request, queryset):
        # Здесь убираем '__id__exact' и используем только прямой ForeignKey lookup
        if self.value():
            return queryset.filter(model_sneaker__brand=self.value())
        return queryset


class ModelSneakerFilter(admin.SimpleListFilter):
    # Название фильтра в панели администратора
    title = _('Модель')

    # Параметр для URL (используется для фильтрации)
    parameter_name = 'model_sneaker'

    def lookups(self, request, model_admin):
        # Если фильтр по бренду выбран, показываем модели для выбранного бренда
        brand_id = request.GET.get('brand')
        from api.models import ModelSneaker  # Импортируем модель
        if brand_id:
            return [(model.id, model.name) for model in ModelSneaker.objects.filter(brand__id=brand_id)]
        # Если бренд не выбран, показываем все модели
        return [(model.id, model.name) for model in ModelSneaker.objects.all()]

    def queryset(self, request, queryset):
        # Фильтруем queryset по выбранной модели
        if self.value():
            return queryset.filter(model_sneaker__id=self.value())
        return queryset
