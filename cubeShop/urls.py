import project
from project import urls
from django.urls import include, path

 
urlpatterns = [
   path('', include(project.urls)),
]