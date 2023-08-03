from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from django.forms import ModelForm

from .models import Category, Product, Brand, TYPE, Tax_Type, Unit, Offer, STATUS, ProductReview


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'cid': forms.TextInput(
                attrs={'class': 'form-control col-6', 'readonly': 'readonly', 'style': 'background:transparent'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Category Name', 'style': 'background:transparent'}),
            'parent': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'icon': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'banner': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'featured': forms.NullBooleanSelect(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'meta_title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Meta Title', 'style': 'background:transparent'}),
            'status': forms.Select(choices=STATUS, attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'meta_description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '5', 'cols': '10', 'placeholder': 'Meta Description',
                       'style': 'background:transparent'}),
        }


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'bid': forms.TextInput(
                attrs={'class': 'form-control col-6', 'readonly': 'readonly', 'style': 'background:transparent'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Brand Name', 'style': 'background:transparent'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'featured': forms.NullBooleanSelect(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'status': forms.Select(choices=STATUS, attrs={'class': 'form-control', 'placeholder': 'Full Name',
                                                          'style': 'background:transparent'}),
            'meta_title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Meta Title', 'style': 'background:transparent'}),
            'meta_description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '5', 'cols': '10', 'placeholder': 'Meta Description',
                       'style': 'background:transparent'}),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'pid': forms.TextInput(
                attrs={'class': 'form-control col-6', 'readonly': 'readonly', 'style': 'background:transparent'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Product Name', 'style': 'background:transparent'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'brand': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'tax': forms.NumberInput(attrs={'class': 'form-control', 'value': '5', 'style': 'background:transparent'}),
            'unit': forms.Select(choices=Unit, attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'pack_size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'style': 'background:transparent'}),
            'min_qty': forms.NumberInput(attrs={'class': 'form-control', 'value': '1', 'style': 'background:transparent'}),
            'type': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}, choices=TYPE),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'barcode': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Product Barcode', 'style': 'background:transparent'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'hover_image': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'price': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '0.00', 'style': 'background:transparent'}),
            'old_price': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '0.00', 'style': 'background:transparent'}),
            'tax_type': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'},
                                     choices=Tax_Type),
            'currency': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'qty': forms.NumberInput(attrs={'class': 'form-control', 'value': '5', 'style': 'background:transparent'}),
            'sku': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'SKU', 'style': 'background:transparent'}),
            'offer': forms.Select(choices=Offer, attrs={'class': 'form-control', 'placeholder': 'Full Name',
                                                        'style': 'background:transparent'}),
            'cod': forms.NullBooleanSelect(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'featured': forms.NullBooleanSelect(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Description', 'style': 'background:transparent'}),
            'meta_title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Meta Title', 'style': 'background:transparent'}),
            'meta_description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '5', 'cols': '10', 'placeholder': 'Meta Description',
                       'style': 'background:transparent'}),
            'meta_image': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'status': forms.Select(choices=STATUS, attrs={'class': 'form-control', 'placeholder': 'Full Name',
                                                          'style': 'background:transparent'}),
        }


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write Review'}))

    class Meta:
        model = ProductReview
        fields = ('review', 'rating')
