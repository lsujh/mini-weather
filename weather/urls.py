from django.urls import path
from .views import index, existingdata_list


urlpatterns = [
    path('weather/<str:city>/<str:data_from>/<str:data_to>/',
         existingdata_list, name='data_list1'),
    path('weather/', existingdata_list, name='data_list'),
    path('', index, name='index'),
]
