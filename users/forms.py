from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
import re



def check_uppercase(value):
	if not re.findall('[A-Z]', value):
		raise ValidationError('Password need at least one uppercase letter.')
	return value


def check_lowercase(value):
	if not re.findall('[a-z]', value):
		raise ValidationError('Password need at least one lowercase letter.')
	return value


def check_firstdigit(value):
	if value[0].isdigit():
		raise ValidationError('First digit must not be a digit')
	return value


class UserSignupForm(UserCreationForm):
	username = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Username'})
	)
	email = forms.EmailField(
		widget=forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Email'})
	)
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'Placeholder': 'password'}),
		validators=[MinLengthValidator(8), check_uppercase, check_lowercase, check_firstdigit]
	)
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'Placeholder': 'confirm password'})
	)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

