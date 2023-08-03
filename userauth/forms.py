from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import User, Profile


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class MobileLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MobileLoginForm, self).__init__(*args, **kwargs)

    phone = forms.CharField(max_length=11, help_text='Required', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '01XXXXXXXXX'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class OTPForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(OTPForm, self).__init__(*args, **kwargs)

    otp = forms.CharField(max_length=6, help_text='Required', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your OTP'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class UpdateUserPasswordForm(forms.ModelForm):
    old_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
