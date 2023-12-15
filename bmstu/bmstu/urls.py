"""
URL configuration for CubeSatStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import HomeF
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from CubeSat import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),


    path('', views.ProductList, name='product_list'),
    path('product_detail/<int:id>/', views.GetProductDetail, name='product_detail'),
    path('deactivate/<int:product_id>/', views.deactivate_product, name='deactivate_product'),
    path(r'products/', views.get_list_of_products, name='get_list_of_products'),
    path(r'orders/', views.get_list_of_orders, name='get_list_of_orders'),
    path(r'add_product_to_order', views.add_product_to_order, name='add_product_to_order'),
    path(r'add_product/', views.add_product, name='add_product'),
    path(r'product/<int:id>', views.get_product, name='get_product'),
    path(r'get_order/<int:id>', views.get_order, name='get_order'),
    path(r'update_price/<int:id>', views.update_price, name='update_price'),
    path(r'delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
