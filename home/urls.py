from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('products/', product_list_view, name='home_product'),
    path('product/<slug>/', product_details, name='product_details'),

    path('location/<slug>/', location_product_list_view, name='product_location'),

    path('category/', category_list_view, name='home_category'),
    path('category/<slug>/', category_product_list_view, name='category_product_list'),

    # Brand
    path('brand/', brand_list_view, name='home_brand'),
    path('brand/<slug>/', brand_product_list_view, name='brand_product_list'),

    # Vendor
    path('vendor/', vendor_list_view, name='home_vendor'),
    path('vendor/<slug>/', vendor_details_view, name='home_vendor_details'),

    # Tags
    path('products/tag/<slug:tag_slug>', tag_list, name='tags'),

    # Add Review
    path('ajax-add-review/<slug>/', ajax_add_review, name='ajax-add-review'),

    # Search & Filter product
    path('search/', search_view, name='home_search'),
    path('filter-products/', filter_product, name='filter-product-shop'),
]
