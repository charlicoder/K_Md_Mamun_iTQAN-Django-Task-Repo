from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserSignupForm


class UserSignupView(CreateView):
	form_class = UserSignupForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('home')
