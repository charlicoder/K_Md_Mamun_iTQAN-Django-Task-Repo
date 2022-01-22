from django.db import models

# Create your models here.


class Category(models.Model):
	title = models.CharField(max_length=50, blank=False, null=False)
	image = models.ImageField(upload_to='categories', blank=True, null=True)

	def __str__(self):
		return self.title



class Product(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)
	image = models.ImageField(upload_to='products', blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)


	def __str__(self):
		return self.name