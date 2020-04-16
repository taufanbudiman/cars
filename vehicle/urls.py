from django.contrib import admin
from django.urls import path

from .views import views
from .views.carbrand import CarBrandlist, CarBrandCreate, CarBrandDelete, CarBrandUpdate, CarBrandDetail
from .views.carmodel import CarModellist, CarModelCreate, CarModelDelete, CarModelUpdate, CarModelDetail

app_name = 'vehicle'
urlpatterns = [
    path('', views.index, name='index'),
    path('carbrand/', CarBrandlist.as_view(), name="carbrand_list" ),
    path('carbrand/add/', CarBrandCreate.as_view(), name="carbrand_add" ),
    path('carbrand/<pk>/delete/', CarBrandDelete.as_view(), name="carbrand_delete" ),
    path('carbrand/<pk>/update/', CarBrandUpdate.as_view(), name="carbrand_update" ),
    path('carbrand/<pk>/detail/', CarBrandDetail.as_view(), name="carbrand_detail" ),

    path('carmodel/', CarModellist.as_view(), name="carmodel_list" ),
    path('carmodel/add/', CarModelCreate.as_view(), name="carmodel_add" ),
    path('carmodel/<pk>/delete/', CarModelDelete.as_view(), name="carmodel_delete" ),
    path('carmodel/<pk>/update/', CarModelUpdate.as_view(), name="carmodel_update" ),
    path('carmodel/<pk>/detail/', CarModelDetail.as_view(), name="carmodel_detail" ),
]