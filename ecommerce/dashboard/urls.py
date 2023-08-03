from django.urls import path

from .views import *

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('admin/profile/<str:username>', view_profile, name='profile'),
    path('admin/change-password/', ChangePasswordView.as_view(), name='update_password'),
    path('admin/deactivate-profile/', deactivate_profile, name='deactivate_profile'),
    path('products/', Products, name='products'),
    path('product/create/', AddNewProduct, name='add_product'),
    path('product/update/<str:slug>', updateProduct, name='update_product'),
    path('product/delete/<str:slug>/', delete, name='delete_product'),
    path('category/', Category_show, name='category'),
    path('category/search/', category_search, name='search_category'),
    path('category/create/', Category_add, name='add_category'),
    path('category/update/<str:slug>/', Category_update, name='update_category'),
    path('category/delete/<str:slug>/', deleteCategory, name='delete_category'),
    path('brand/', showbrand, name='brand'),
    path('update_brand/', brandupdate, name='update_brand'),
    path('customers/', Customers, name='customers'),
    path('deactivate_customer/<int:id>/', deactivate_customer, name='deactivate_customer'),
    path('activate_customer/<int:id>/', activate_customer, name='activate_customer'),
    path('staff/', Staffs, name='staff'),
    path('deactivate_staff/<int:id>/', deactivate_staff, name='deactivate_staff'),
    path('activate_staff/<int:id>/', activate_staff, name='activate_staff'),
]

