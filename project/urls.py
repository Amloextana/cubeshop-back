
from django.contrib import admin
from django.urls import path
 
from django.contrib import admin
from project import views
from django.urls import include, path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from rest_framework import permissions
from rest_framework import routers
 
router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

 
urlpatterns = [
   path('', include(router.urls)),

   #COMPONENTS
   path(r'components/', views.get_components, name='components-list'),#GET - получить список всех компонентов
   path(r'components/post/', views.post_component, name='components-post'),#POST - добавить новый компонент
   path(r'components/<int:pk>/image/post/', views.postImageToComponent), #POST - добавить изображение
   path(r'components/<int:pk>/', views.get_component, name='components-detail'),#GET - получить один компонент
   path(r'components/<int:pk>/put/', views.put_component, name='components-put'),#PUT - обновить один компонент
   path(r'components/<int:pk>/delete/', views.delete_component, name='components-delete'),#PUT - удалить один компонент
   path(r'components/<int:pk>/add_to_application/', views.add_to_application, name='components-add-to-application'),#POST - добавить компонент в заявку
 
   #APPLICATIONS 
   path(r'applications/', views.get_applications, name='applications-list'),#GET - получить список всех заявок
   path(r'applications/<int:pk>/', views.get_application, name='applications-detail'),#GET - получить одну заявку
   # path(r'applications/<int:pk>/track/put/', views.put_track, name='applications-put'),#PUT - обновить одну заявку
   path(r'applications/<int:pk>/delete/', views.delete_application),#DELETE - удалить одну заявку
   path(r'applications/<int:pk>/update_by_user/', views.update_by_user, name='update_by_user'),#PUT - изменение статуса пользователем
   path(r'applications/<int:pk>/update_by_admin/', views.update_by_admin, name='update_by_admin'),#PUT - изменение статуса модератором

   #COMPONENTS IN APPLICATION
   path(r"applications/<int:application_id>/delete_component/<int:component_id>/", views.delete_component_from_application),#DELETE - удалить компонент из заявки
   path(r"applications/<int:application_id>/update_amount/<int:component_id>/", views.update_component_amount),#PUT - изменить кол-во компонентов в заявке
   
   #AUTH
   path('create/',  views.create, name='create'),
   path('login/',  views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout'),
   path('user_info/', views.user_info, name='user_info'),
   #  path('cart/', views.get_current_cart, name='get_current_cart'),
    
   path('async_token/<int:pk>/', views.async_token, name="async_token"),

   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('admin/', admin.site.urls),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
 
