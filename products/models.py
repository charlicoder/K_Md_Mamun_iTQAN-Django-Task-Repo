from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount

# Create your models here.


class Category(models.Model):
	title = models.CharField(max_length=50, blank=False, null=False)
	image = models.ImageField(upload_to='categories', blank=True, null=True)

	def __str__(self):
		return self.title


class Product(models.Model, HitCountMixin):
	name = models.CharField(max_length=50, blank=False, null=False)
	image = models.ImageField(upload_to='products', blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	hit_count_generic = GenericRelation(
		HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
	
	@property
	def current_hit_count(self):
		return self.hit_count.hits
		
	def __str__(self):
		return self.name