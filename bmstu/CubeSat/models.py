from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Customer(User):
    class Meta:
        verbose_name_plural = "Покупатели"


class Employer(User):

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
    moderator = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Заказы"


class Product(models.Model):
    class ProductCategoryChoices(models.TextChoices):
        POWER_MODULES = "Power Modules"
        STRUCTURES = "Structures"
        SOLAR_PANELS = "Solar Panels"

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category_of_product = models.CharField(max_length=30, choices=ProductCategoryChoices.choices)
    id_in_category = models.CharField()  # change to FK

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Детали"


class OrdersToProducts(models.Model):
    request = models.ForeignKey(Orders, on_delete=models.CASCADE)
    detail = models.ForeignKey(Product, on_delete=models.CASCADE)


class PowerModules(models.Model):
    name = models.CharField()
    voltage = models.DecimalField(max_digits=16, decimal_places=2)  # В, V
    max_total_current_of_solar_panel = models.IntegerField()  # мА, mA
    max_current_of_solar_panel_in_channel = models.DecimalField(max_digits=16, decimal_places=2)  # мА, mA
    max_power_consumption = models.DecimalField(max_digits=16, decimal_places=2)  # Вт, w

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Блоки питания"


class Structures(models.Model):
    name = models.DecimalField(max_digits=16, decimal_places=2)
    length = models.DecimalField(max_digits=16, decimal_places=2)
    width = models.DecimalField(max_digits=16, decimal_places=2)
    height = models.DecimalField(max_digits=16, decimal_places=2)
    amount_of_push_springs = models.IntegerField()
    min_operating_temperature = models.DecimalField(max_digits=16, decimal_places=2)
    max_operating_temperature = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Корпусы"


class SolarPanels(models.Model):
    name = models.CharField()
    type_of_element = models.CharField()
    open_circuit_voltage = models.DecimalField(max_digits=16, decimal_places=2)
    short_circuit_current = models.DecimalField(max_digits=16, decimal_places=2)

    class Meta:
        verbose_name_plural = "Солнечные панели"