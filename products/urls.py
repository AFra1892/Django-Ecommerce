from django.urls import path
from . import views

urlpatterns = [
    path("" , views.product_list_view , name='product-list'),
    path("<int:id>",views.product_detail_view , name ='product-detail'),
    # path("<int:id>/edit/" , views.product_edit_view , name="product-edit"),
    # path("create/" , views.product_create_view , name="product-create")
]
