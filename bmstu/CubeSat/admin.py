from django.contrib import admin
from .models import Orders, OrdersToProducts, Product, Customer, Employer, PowerModules


class ProductsInLine(admin.TabularInline):
    model = Product
    extra = 1


class SalesToProductsInline(admin.TabularInline):  # Или используйте StackedInline, если предпочитаете другой вид отображения
    model = OrdersToProducts
    extra = 1  # Количество пустых форм для добавления товаров
    inlines = [ProductsInLine]  # Добавляем инлайн для Sales


class SalesAdmin(admin.ModelAdmin):
    list_display = ('status', 'created_at', 'formed_at', 'completed_at', 'moderator', 'customer')
    list_filter = ('status', 'created_at', 'formed_at', 'completed_at', 'moderator', 'customer')
    inlines = [SalesToProductsInline]  # Добавляем инлайн для Sales


admin.site.register(Orders, SalesAdmin)
admin.site.register(Product)
admin.site.register(OrdersToProducts)
admin.site.register(Employer)
admin.site.register(Customer)
admin.site.register(PowerModules)
