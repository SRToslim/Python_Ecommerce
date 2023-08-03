from django.contrib import messages
from django.shortcuts import render, redirect

from userauth.models import Profile, User

from userauth.forms import UpdateUserForm, UpdateProfileForm


def UserDashboard(request):
    if request.user.is_authenticated:
        return render(request, 'customer/dashboard.html')
    else:
        return redirect('login')


def CustomerInfo(request):
    if request.user.is_authenticated:
        if request.method == 'post' or request.method == 'POST':
            user = User.objects.all()
            UserForm = UpdateUserForm(request.POST, instance=request.user)
            profileForm = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if UserForm.is_valid() and profileForm.is_valid():
                UserForm.save()
                profileForm.save()

                messages.success(request, 'Your profile is updated successfully')
            return render(request, 'customer/profile.html')
        else:
            prof = Profile.objects.get(user=request.user.id)
            active = str(prof.user.last_login - prof.date_joined).split('.')[0]

            return render(request, 'customer/profile.html', locals())

    else:
        return redirect('login')


def CustomerOrder(request):
    if request.user.is_authenticated:

        return render(request, 'customer/order.html')
    else:
        return redirect('login')
