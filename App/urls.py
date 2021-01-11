from . import views
from django.urls import path

app_name='App'

urlpatterns=[
    path('',views.index,name='index'),
    path('search',views.search,name='search'),
 
    path('category',views.category,name='category'),
    path('category_detail/<int:id>/',views.category_detail,name='category_detail'),
    path('category_response',views.category_response,name='category_response'),

    path('material',views.material,name='material'),
    path('material_detail/<int:id>/',views.material_detail,name='material_detail'),
    path('material_response',views.material_response,name='material_response'),

    path('product',views.product,name='product'),
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),
    path('product_response',views.product_response,name='product_response'),

    path('supplier',views.supplier,name='supplier'),
    path('supplier_detail/<int:id>/',views.supplier_detail,name='supplier_detail'),
    path('supplier_response',views.supplier_response,name='supplier_response'),
    
    path('foreign_purchase',views.foreign_purchase,name='foreign_purchase'),
    path('standard_purchase',views.standard_purchase,name='standard_purchase'),

]
