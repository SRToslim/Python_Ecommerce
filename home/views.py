from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.template.loader import render_to_string

from products.models import Category, Product, Vendor, Brand, ProductReview, Location

from products.forms import ProductReviewForm
from taggit.models import Tag


def home(request):
    products = Product.objects.filter(status='published')
    new_products = Product.objects.filter(status='published').order_by('-date')
    recent_product = Product.objects.filter(status='published').order_by('-date')[:3]

    return render(request, 'base.html', locals())


def product_list_view(request):
    products = Product.objects.filter(status='published').order_by('-id')

    context = {
        'products': products
    }

    return render(request, 'product-list.html', context)


def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(slug=slug)[:4]

    reviews = ProductReview.objects.filter(product=product).order_by('-date')
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    review_form = ProductReviewForm()

    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False

    p_image = product.gallery.all()

    context = {
        'p': product,
        'make_review': make_review,
        'p_image': p_image,
        'review_form': review_form,
        'average_rating': average_rating,
        'reviews': reviews,
        'related_products': related_products,
    }

    return render(request, 'product/details.html', context)


def category_list_view(request):
    categories = Category.objects.all()

    return render(request, 'category.html', locals())


def category_product_list_view(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(status='published', category=category)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category-product-list.html', context)


def vendor_list_view(request):
    vendors = Vendor.objects.all().annotate(product_count=Count('vendor'))

    context = {
        'vendors': vendors
    }

    return render(request, 'vendor.html', context)


def vendor_details_view(request, slug):
    vendor = Vendor.objects.get(slug=slug)
    products = Product.objects.filter(status='published', vendor=vendor)

    context = {
        'vendor': vendor,
        'products': products
    }

    return render(request, 'vendor-details.html', context)


def brand_list_view(request):
    brands = Brand.objects.all()

    context = {
        'brands': brands
    }

    return render(request, 'brand.html', context)


def brand_product_list_view(request, slug):
    brand = Brand.objects.get(slug=slug)
    products = Product.objects.filter(status='published', brand=brand)

    context = {
        'brand': brand,
        'products': products
    }

    return render(request, 'brand-product-list.html', context)


def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_statas='published').order_by('-id')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        'products': products,
        'tag': tag
    }

    return render(request, 'core/tag.html', context)


def ajax_add_review(request, slug):
    product = Product.objects.get(slug=slug)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews
        }
    )


def search_view(request):
    query = request.GET.get('q')

    products = Product.objects.filter(title__icontains=query).order_by('-date')

    context = {
        'products': products,
        'query': query,
    }

    return render(request, 'core/search.html', context)


def filter_product(request):
    categories = request.GET.getlist('category[]')
    vendors = request.GET.getlist('vendor[]')

    min_price = request.GET['min_price']
    max_price = request.GET['max_price']

    products = Product.objects.filter(product_statas='published').order_by('-id').distinct()

    products = products.filter(price__gte=min_price)
    products = products.filter(price__lte=max_price)

    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()

    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors).distinct()

    data = render_to_string('core/async/product-list.html', {'products': products})
    return JsonResponse({
        'data': data
    })


def location_product_list_view(request, slug):
    location = Location.objects.get(slug=slug)
    products = Product.objects.filter(status='published', location=location)

    context = {
        'location': location,
        'products': products,
    }

    return render(request, 'location-product-list.html', context)
