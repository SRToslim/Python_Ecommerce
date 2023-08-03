from .models import Category, Brand, Vendor


def default(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    vendors = Vendor.objects.all()

    return {
        'categories': categories,
        'brands': brands,
        'vendors': vendors,
    }
