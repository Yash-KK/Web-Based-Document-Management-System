from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='d-index'),
    path("staff",views.staff,name='d-staff'),
    path("products",views.products,name='d-products'),
    path("products/delete/<int:id>",views.delete_product,name='d-delete'),
    path("delete/<int:id>",views.staff_delete,name='d-staff-delete'),
    path("products/edit/<int:id>",views.edit_product,name='d-edit'),
    path("edit/<int:id>",views.staff_edit,name='d-staff-edit'),
    path("orders",views.orders,name='d-orders')
]    