from django.contrib import admin

from .models import *


class ProductImageAdmin(admin.TabularInline):
    model = ProductImages


class ProductVideoAdmin(admin.TabularInline):
    model = ProductVideo


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ProductVideoAdmin]
    readonly_fields = ['pid']
    list_display = [
        'name',
        'product_image',
        'sku',
        'category',
        'brand',
        'price',
        'offer',
        'cod',
        'featured',
        'status',
    ]


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['cid']
    list_display = ['name', 'parent', 'featured', 'status']


class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ['bid']
    list_display = ['name', 'brand_image', 'featured', 'status']


class VendorAdmin(admin.ModelAdmin):
    readonly_fields = ['vid']
    list_display = ['title', 'vendor_image', 'contact', 'address']


class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ['lid']
    list_display = ['title', 'lid', 'address', 'status', 'date']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Location, LocationAdmin)
