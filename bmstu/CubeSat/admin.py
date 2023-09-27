from django.contrib import admin
from .models import *


from django.contrib import admin

class AttributesValuesInline(admin.TabularInline):
    model = AttributesValues
    extra = 1

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj:
            formset.form.base_fields['attribute_ref'].queryset = Attributes.objects.filter(category_ref=obj.category_ref)
        else:
            formset.form.base_fields['attribute_ref'].queryset = Attributes.objects.none()
        return formset


class AttributesInline(admin.TabularInline):
    model = Attributes
    extra = 1


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'category_ref')
    inlines = [AttributesValuesInline]


class CategoriesAdmin(admin.ModelAdmin):
    inlines = [AttributesInline]


class OrdersToProductsInline(admin.TabularInline):  # Или StackedInline, в зависимости от вида отображения, который вы предпочитаете
    model = OrdersToProducts
    extra = 1  # Это позволит добавлять несколько продуктов в заказ одновременно

class OrdersAdmin(admin.ModelAdmin):
    inlines = [OrdersToProductsInline]


admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(AttributesValues)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Customer)
admin.site.register(Employer)
admin.site.register(OrdersToProducts)
