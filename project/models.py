from decimal import Decimal
from django.db import models 
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import UserManager,User, PermissionsMixin, AbstractBaseUser
  
class Components(models.Model): 
    title = models.CharField(max_length=50, blank=True, null=True) 
    category = models.CharField(max_length=50, blank=True, null=True) 
    description = models.TextField(blank=True, null=True) 
    features = models.TextField(blank=True, null=True) 
    available = models.BooleanField(blank=True,default=True, null=True) 
    image = models.CharField(max_length=255, blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    
    class Meta: 
        verbose_name_plural = "Components" 
        managed = True 
    def __str__(self): 
        return self.title 


class NewUserManager(UserManager):
    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields) 
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin): 

    email = models.CharField(max_length=500,unique=True) 
    password = models.CharField(max_length=500, blank=True, null=True) 
    is_moderator = models.BooleanField(blank=True, null=True) 
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    objects =  NewUserManager()
    
    class Meta: 
        verbose_name_plural = "Users" 
        managed = True 
    def __str__(self): 
        return self.email 


class Applications(models.Model): 
    STATUS_CHOICES = ( 
        (1, 'Черновик'), 
        (2, 'Удален'), 
        (3, 'Сформирован'), 
        (4, 'Завершен'), 
        (5, 'Отклонен'), 
    ) 
  
    status = models.CharField(choices=STATUS_CHOICES,default=1,max_length=20) 
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)    
    formed_at = models.DateTimeField(blank=True, null=True) 
    completed_at = models.DateTimeField(blank=True, null=True) 
    moderator = models.ForeignKey(Users, on_delete=models.CASCADE,blank=True, null=True) 
    customer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='applications_customer_set', blank=True, null=True) 
    delivery_token = models.IntegerField(blank=True, null=True)
    class Meta: 
        verbose_name_plural = "applications" 
        managed = True 
    def __str__(self): 
        return self.title 
  
  
class Applicationscomponents(models.Model): 
    amount = models.IntegerField(default=1,blank=True, null=True) 
    application = models.ForeignKey(Applications, on_delete=models.CASCADE, blank=True, null=True) 
    component = models.ForeignKey(Components, on_delete=models.CASCADE, blank=True, null=True)
  
    class Meta: 
        managed = True

