import random

from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserRegistrationForm, UserLoginForm, MobileLoginForm, OTPForm
from .models import User
from .tokens import account_activation_token


def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    elif not request.user.is_authenticated:
        if request.method == 'post' or request.method == 'POST':
            form = UserRegistrationForm(request.POST or None)
            check_user = User.objects.filter(email='email').first()
            if check_user:
                messages.error(request, f'User already exists, Try login.')
            else:
                if form.is_valid():
                    user = form.save(commit=False)
                    user.is_active = False
                    user.ip = get_client_ip(request)
                    user.save()

                    activateEmail(request, user, form.cleaned_data.get('email'))
                    return HttpResponseRedirect(reverse('index'))

                else:
                    for error in list(form.errors.values()):
                        messages.error(request, error)
        else:
            form = UserRegistrationForm()

    return render(request, 'users/register.html', locals())


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('users/email_confirmation.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_verify = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')

    return HttpResponseRedirect(reverse('index'))


def get_client_ip(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def email_login(request):
    if request.user.is_authenticated:
        messages.success(request, f'Hey you are already Logged In')
        return HttpResponseRedirect(reverse('index'))
    elif not request.user.is_authenticated:
        if request.method == 'POST' or request.method == 'post':
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                )
                if user:
                    user.last_ip = get_client_ip(request)
                    user.save()
                    login(request, user)
                    messages.success(request, f'Hey {user.username}, You are successfully login')
                    return HttpResponseRedirect(reverse('index'))
                else:
                    messages.error(request, f'User dose not exist, Create an Account.')
                    return redirect('login')
            else:
                for key, error in list(form.errors.items()):
                    if key == 'captcha' and error[0] == messages.warning(request, 'The reCAPTCHA field is required.'):
                        messages.error(request, 'You must pass the reCAPTCHA test')
                    messages.error(request, error)

    form = UserLoginForm()

    return render(request, 'users/login.html', locals())


def mobile_login(request):
    if request.user.is_authenticated:
        messages.success(request, f'Hey you are already Logged In')
        return HttpResponseRedirect(reverse('index'))
    elif not request.user.is_authenticated:
        if request.method == 'POST' or request.method == 'post':
            form = MobileLoginForm(request=request, data=request.POST)
            user = User.objects.filter(phone='phone').first()
            if form.is_valid():
                otp = str(random.randint(100000, 999999))
                user.otp = otp
                user.save()
                send_otp(form, otp)
                request.session['phone'] = form
                return redirect('otp')
            else:
                for key, error in list(form.errors.items()):
                    if key == 'captcha' and error[0] == messages.warning(request, 'The reCAPTCHA field is required.'):
                        messages.error(request, 'You must pass the reCAPTCHA test')
                    messages.error(request, error)

    form = MobileLoginForm()

    return render(request, 'users/mobile.html', locals())


def login_otp(request):
    if request.user.is_authenticated:
        messages.success(request, f'Hey you are already Logged In')
        return HttpResponseRedirect(reverse('index'))
    elif not request.user.is_authenticated:

        if request.method == 'POST' or request.method == 'post':
            form = OTPForm(request=request, data=request.POST)
            otp = request.POST.get('otp')
            user = User.objects.filter(phone='phone').first()

            if form.is_valid():
                login(request, user)
                messages.success(request, f'Hey {user.username}, You are successfully login')
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('otp'))

    form = OTPForm()

    return render(request, 'users/otp.html', locals())


def logout_view(request):
    logout(request)
    messages.success(request, 'You are successfully logged out from your account.')
    return redirect('login')










