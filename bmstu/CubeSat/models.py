from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Customer(User):
    pass


class Employer(User):

    class PositionChoices(models.TextChoices):
        JUNIOR_MANAGER = 'Junior manager'
        SENIOR_MANAGER = 'Senior manager'

    position = models.CharField(max_length=30, choices=PositionChoices.choices, default=PositionChoices.JUNIOR_MANAGER)
    is_manager = models.BooleanField(default=True)


class Request(models.Model):

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


class Product(models.Model):

    class ProductCategoryChoices(models.TextChoices):
        POWER_MODULES = "Power Modules"
        STRUCTURES = "Structures"
        SOLAR_PANELS = "Solar Panels"

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
 #   category_of_product = models.CharField(max_length=30, choices=ProductCategoryChoices.choices, default=S)
  #  id_in_category = models.CharField()


class PowerModules(models.Model):
    voltage = models.IntegerField()
    max_current_of_solar_panel = models.IntegerField()


class RequestsToDetails(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    detail = models.ForeignKey(Product, on_delete=models.CASCADE)

