import _datetime
import os
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from products.models import Product, Category, Brand

from userauth.models import Profile, User

from products.forms import ProductForm, CategoryForm, BrandForm

from userauth.forms import UpdateProfileForm, UpdateUserPasswordForm, UpdateUserForm


def Dashboard(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin' or request.user.user_type == 'staff':
            day = datetime.now().date()
            return render(request, 'dashboard/base.html', locals())
    else:
        return redirect('login')


def view_profile(request, username):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin' or request.user.user_type == 'staff':
            if request.method == 'post' or request.method == 'POST':
                user = User.objects.get(username=username)
                UserForm = UpdateUserForm(request.POST, instance=request.user)
                profileForm = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
                if UserForm.is_valid() and profileForm.is_valid():
                    UserForm.save()
                    profileForm.save()

                    messages.success(request, 'Your profile is updated successfully')
                return redirect('profile', user.id)
            else:
                prof = Profile.objects.get(user=request.user.id)
                active = str(prof.user.last_login - prof.date_joined).split('.')[0]

                return render(request, 'dashboard/profile.html', locals())
        else:
            return redirect('index')
    else:
        return redirect('login')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'dashboard/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('logout')


def deactivate_profile(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer':
            messages.warning(request, 'You are a Super User.')
            return redirect('profile', request.user.username)
        elif request.user.user_type == 'admin' or request.user.user_type == 'staff':
            user = request.user
            user.is_active = False
            user.save()
            logout(request)
            messages.success(request, 'Profile successfully disabled.')
            return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect(to='login')


def Products(request):
    if request.user.is_authenticated and request.user.user_type == 'developer' or request.user.user_type == 'admin' \
            or request.user.user_type == 'staff':
        products = Product.objects.all()

        p = Paginator(Product.objects.all().order_by('-id'), 15)
        page = request.GET.get('page')
        products = p.get_page(page)
        nums = 'a' * products.paginator.num_pages
        return render(request, 'product/show.html', locals())
    else:
        return redirect('login')


def AddNewProduct(request):
    if request.user.is_authenticated and request.user.user_type == 'developer' or request.user.user_type == 'admin'\
            or request.user.user_type == 'staff':
        if request.method == 'post' or request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                slug = product.name.replace(' ', '-')
                product.slug = slug.lower()
                product.save()
            messages.success(request, 'Product successfully added.')
            return redirect('products')
        else:
            form = ProductForm()
            return render(request, 'product/create.html', {'form': form})
    else:
        messages.warning(request, "You don't have permission to add product")
        return redirect('login')


def updateProduct(request, slug):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin' \
                or request.user.user_type == 'staff':
            if request.method == 'post' or request.method == 'POST':
                product = Product.objects.get(slug=slug)
                form = ProductForm(request.POST, request.FILES, instance=product)
                if form.is_valid():
                    product = form.save(commit=False)
                    slug = product.name.replace(' ', '-')
                    product.slug = slug.lower()
                    form.save()
                    messages.success(request, 'Product successfully updated.')
                    return redirect(to='products')
            else:
                product = Product.objects.get(slug=slug)
                form = ProductForm(instance=product)
                return render(request, 'product/create.html', locals())
    else:
        return redirect('login')


def delete(request, slug):
    product = Product.objects.get(slug=slug)
    if product.image:
        os.remove(product.image.path)
        os.remove(product.hover_image.path)
    product.delete()
    messages.success(request, 'Product Deleted successfully.')
    return redirect(to='products')


def Category_show(r):
    if r.user.is_authenticated:
        if r.user.user_type == 'developer' or r.user.user_type == 'admin' or r.user.user_type == 'staff':
            category = Category.objects.all()
            return render(r, 'category/show.html', locals())
    else:
        return redirect('login')


def category_search(request):
    query = request.GET.get('q')
    category = Category.objects.filter(name__icontains=query)

    return render(request, 'category/search.html', locals())


def Category_add(request):
    if request.user.is_authenticated and request.user.user_type == 'developer' or request.user.user_type == 'admin'\
            or request.user.user_type == 'staff':
        if request.method == 'post' or request.method == 'POST':
            form = CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                cat = form.save(commit=False)
                slug = cat.name.replace(' ', '-')
                cat.slug = slug.lower()
                cat.save()
            messages.success(request, 'Category successfully added.')
            return redirect('category')
        else:
            form = CategoryForm()
            return render(request, 'category/create.html', {'form': form})
    else:
        return redirect('login')


def Category_update(request, slug):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin' \
                or request.user.user_type == 'staff':
            if request.method == 'post' or request.method == 'POST':
                category = Category.objects.get(slug=slug)
                form = CategoryForm(request.POST, request.FILES, instance=category)
                if form.is_valid():
                    category = form.save(commit=False)
                    slug = category.name.replace(' ', '-')
                    category.slug = slug.lower()
                    form.save()
                    messages.success(request, 'Category successfully added.')
                    return redirect(to='category')
            else:
                category = Category.objects.get(slug=slug)
                form = CategoryForm(instance=category)
                return render(request, 'category/create.html', locals())
    else:
        return redirect('login')


def deleteCategory(request, slug):
    category = Category.objects.get(slug=slug)
    if category.image:
        os.remove(category.icon.path)
        os.remove(category.image.path)
        os.remove(category.banner.path)
    category.delete()
    messages.success(request, 'Category Deleted Successfully.')
    return redirect(to='category')


def showbrand(r):
    return render(r, 'brand/show.html')


def brandupdate(r, id):
    return render(r, 'brand/update.html')


def Customers(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin' \
                or request.user.user_type == 'staff':
            customers = Profile.objects.all()

            context = {
                'customers': customers
            }

            return render(request, 'dashboard/customer.html', context)
    else:
        return redirect('dashboard')


def deactivate_customer(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(id=id)
        user.is_active = False
        user.save()
        messages.warning(request, 'Customer de-activate is successfully.')
        return redirect(to='customers')


def activate_customer(request, id):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin' \
                or request.user.user_type == 'staff':
            user = User.objects.get(id=id)
            user.is_active = True
            user.save()
            messages.success(request, 'Customer is successfully activate.')
            return redirect(to='customers')


def Staffs(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin' \
                or request.user.user_type == 'staff':
            staffs = Profile.objects.all()
            return render(request, 'dashboard/staff.html', locals())
        else:
            return redirect('dashboard')
    else:
        return redirect('login')


def deactivate_staff(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(id=id)
        user.is_active = False
        user.save()
        messages.warning(request, 'Customer de-activate is successfully.')
        return redirect(to='staff')


def activate_staff(request, id):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin':
            user = User.objects.get(id=id)
            user.is_active = True
            user.save()
            messages.success(request, 'Customer is successfully activate.')
            return redirect(to='staff')


def brand_view(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'developer' or request.user.user_type == 'admin' \
                or request.user.user_type == 'staff':
            brands = Brand.objects.all()
    else:
        return redirect('login')
