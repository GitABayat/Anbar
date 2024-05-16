from django.urls import path
from StoreMenuApp import views
# from django.views.generic import TemplateView

app_name = 'StoreMenuApp'
urlpatterns = [
    # آدرس مربوط به کلاس Crud
    path('Create/', views.Crud.Create, name='Create'),
    path('FindUpdateIndo/', views.Crud.FindUpdateIndo, name='FindUpdateIndo'),
    path('Update/', views.Crud.Update, name='Update'),
    path('Delete/', views.Crud.Delete, name='Delete'),

    # در این بخش آدرس های مروبط به کلاس های DataTable های قرار میگیرد
    # 1-Store
    path('StoreLV/', views.StoreLV.as_view(), name='StoreLV'),
    path('StoreDT/',views.StoreDT.as_view(), name='StoreDT'), 

    # 2-GoodsAndServices 
    path('GoodsAndServicesLV/', views.GoodsAndServicesLV.as_view(), name='GoodsAndServicesLV'),
    path('GoodsAndServicesDT/',views.GoodsAndServicesDT.as_view(), name='GoodsAndServicesDT'),

    # 3-CustomersGroup
    path('CustomersGroupLV/', views.CustomersGroupLV.as_view(), name='CustomersGroupLV'),
    path('CustomersGroupDT/',views.CustomersGroupDT.as_view(), name='CustomersGroupDT'),

    # 4-Customers
    path('CustomersLV/', views.CustomersLV.as_view(), name='CustomersLV'),
    path('CustomersDT/',views.CustomersDT.as_view(), name='CustomersDT'),

    # 5-Recept
    path('', views.ReceptLV.as_view(), name='ReceptLV'),
    path('ReceptDT/',views.ReceptDT.as_view(), name='ReceptDT'),
    
]
