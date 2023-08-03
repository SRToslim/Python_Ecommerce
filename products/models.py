from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
from taggit.managers import TaggableManager

from web_settings.models import Currency

from userauth.models import User

STATUS = {
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in_review', 'In Review'),
    ('published', 'Published'),
}

Offer = {
    ('today_deal', "Today's Deal"),
    ('Savings', 'Great Saving'),
    ('buy1get1', 'Buy 1 Get 1')
}

TYPE = {
    ('physical', 'Physical'),
    ('digital', 'Digital'),
}

PROVIDER = {
    ('youtube', 'YouTube'),
    ('facebook', 'Facebook'),
    ('dailymotion', 'Dailymotion'),
    ('vimeo', 'Vimeo'),
}

Tax_Type = {
    ('flat', 'Flat'),
    ('percent', 'Percent')
}

Unit = {
    ('kg', 'kg'),
    ('pkt', 'pkt'),
    ('gm', 'gm'),
    ('bunch', 'bunch'),
    ('dozen', 'dozen'),
    ('liter', 'liter'),
    ('box', 'box'),
    ('piece', 'piece'),
}

RATING = {
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
}


class NonDeleted(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)

    everything = models.Manager()
    objects = NonDeleted

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


# noinspection PyTypeChecker
class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345")
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', null=True, blank=True, unique=True, default=None)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    icon = models.ImageField(upload_to="category/icon/", blank=True, null=True)
    image = models.ImageField(upload_to="category/image/", blank=True, null=True)
    banner = models.ImageField(upload_to="category/banner/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS, max_length=10, default='published')
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.icon.url))

    def __str__(self):
        return self.name


# noinspection PyTypeChecker
class Brand(models.Model):
    bid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="b_", alphabet="abcdefgh12345")
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', null=True, blank=True, unique=True, default=None)
    image = models.ImageField(upload_to="brand/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS, max_length=10, default='published')
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Brands"

    def brand_image(self):
        return mark_safe('<img src="%s" width="100" height="50">' % (self.image.url))

    def __str__(self):
        return self.name


# noinspection PyTypeChecker
class Vendor(models.Model):
    objects = None
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="v_", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', null=True, blank=True, unique=True, default=None)
    image = models.ImageField(upload_to='vendor/', default='vendor.jpg')
    cover_image = models.ImageField(upload_to='vendor/', default='vendor.jpg')
    description = RichTextUploadingField(null=True, blank=True)
    address = models.CharField(max_length=250, default='Mirpur, Dhaka')
    contact = models.CharField(max_length=100, default='+8801966172000')
    chat_resp_time = models.CharField(max_length=100, default='100')
    shipping_on_time = models.CharField(max_length=100, default='100')
    authentic_rating = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    warranty_period = models.CharField(max_length=100, default='100')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="120" height="30">' % (self.image.url))

    def __str__(self):
        return self.title


class Tags(models.Model):
    pass


class Location(models.Model):
    lid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="l_", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', null=True, blank=True, unique=True, default=None)
    image = models.ImageField(upload_to='location', default='location.jpg', null=True, blank=True)
    address = models.CharField(max_length=250, null=True)
    status = models.CharField(choices=STATUS, max_length=10, default='published')
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Location"

    def location_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='p_', alphabet='abcdefgh12345')
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', null=True, blank=True, unique=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, related_name='brand')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True, related_name='vendor')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='location')
    tax = models.IntegerField(blank=True, null=True, default=5)
    unit = models.CharField(max_length=100, blank=False, null=False, choices=Unit)
    pack_size = models.DecimalField(max_digits=5, decimal_places=3)
    min_qty = models.DecimalField(max_digits=5, decimal_places=2)
    tags = TaggableManager(blank=True)
    type = models.CharField(choices=TYPE, max_length=10, default='physical')
    barcode = models.CharField(unique=True, max_length=30, blank=False, null=False, default=None)
    image = models.ImageField(upload_to="products/", blank=False, null=False)
    hover_image = models.ImageField(upload_to="products/", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tax_type = models.CharField(choices=Tax_Type, max_length=10, default='percent')
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, default='Taka',
                                 related_name='currency')
    qty = models.CharField(max_length=10)
    sku = models.CharField(unique=True, max_length=30, blank=False, null=False, default=None)
    offer = models.CharField(choices=Offer, max_length=10, default=None, null=True, blank=True)
    cod = models.BooleanField(default=True, verbose_name='Cash on Delivery')
    featured = models.BooleanField(default=False)
    description = RichTextUploadingField(null=True, blank=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    meta_image = models.ImageField(upload_to="products/meta/", blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=10, default='in_review')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))

    def __str__(self):
        return self.name

    def sale_price(self):
        if self.old_price:
            new_price = (self.price / self.old_price) * 100
            return new_price


class ProductImages(models.Model):
    images = models.ImageField(upload_to='product-images/', default='product.jpg')
    product = models.ForeignKey(Product, related_name='gallery', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Gallery Images"


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, related_name='video', on_delete=models.SET_NULL, null=True)
    provider = models.CharField(choices=PROVIDER, max_length=100, null=True, blank=True)
    link = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Video"


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.name

    def get_rating(self):
        return self.rating
