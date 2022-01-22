from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Category, Product

class ProductHomeView(LoginRequiredMixin, ListView):
	template_name = 'products/home.html'
	model = Category


class ProductListView(LoginRequiredMixin, ListView):
	template_name = 'products/category-products-list.html'
	model = Product

	def get_context_data(self, **kwargs):
		# import pdb; pdb.set_trace();

		context = super().get_context_data(**kwargs)
		categories = Category.objects.all()
		context['categories'] = categories
		return context

	def get_queryset(self):
		cat_id = self.kwargs.get('id')
		qs = Product.objects.filter(category=cat_id)
		return qs



class ProductDetailView(LoginRequiredMixin, DetailView):
	template_name = 'products/product_detail.html'
	model = Product

	def get_context_data(self, **kwargs):
		# import pdb; pdb.set_trace();

		context = super().get_context_data(**kwargs)
		categories = Category.objects.all()
		context['categories'] = categories
		return context

	def get_object(self):
		pk = self.kwargs.get('id')
		obj = Product.objects.get(id=pk)
		return obj


