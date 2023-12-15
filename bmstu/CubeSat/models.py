from django.db import models
import os

class User(models.Model):
    name = models.CharField(verbose_name="имя")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Customer(User):
    class Meta:
        verbose_name_plural = "Покупатели"


class Moderator(User):

    class PositionChoices(models.TextChoices):
        JUNIOR_MANAGER = 'Junior manager'
        SENIOR_MANAGER = 'Senior manager'

    position = models.CharField(max_length=30, choices=PositionChoices.choices, default=PositionChoices.JUNIOR_MANAGER)
    is_manager = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Сотрудники"


class Orders(models.Model):

    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        IN_PROGRESS = 'In Progress'
        COMPLETED = 'Completed'
        CANCELLED = 'Cancelled'
        DELETED = 'Deleted'

    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    formed_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    moderator = models.ForeignKey(Moderator, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Заказы"


class Categories(models.Model):
    category_name = models.CharField()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category_ref = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='CubeSat/static/images/')
    product_image = models.BinaryField(blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Детали"


class Attributes(models.Model):
    attribute_name = models.CharField()
    category_ref = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.attribute_name


class AttributesValues(models.Model):
    id = models.AutoField(primary_key=True)
    attribute_value = models.CharField()
    attribute_ref = models.ForeignKey(Attributes, on_delete=models.CASCADE, null=True)
    product_ref = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)


class OrdersToProducts(models.Model):
    product_ref = models.ForeignKey(Orders, on_delete=models.CASCADE)
    order_ref = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, default=None)
