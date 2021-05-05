from django.db import models

class Unit(models.Model):

	unit_name = models.CharField(max_length=50,null=True)
	unit_abbv = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.unit_name

class Product(models.Model):

	product_name = models.CharField(max_length=50,null=True)
	product_description = models.CharField(max_length=50,null=True)

	product_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='product_unit', null=True)

	def __str__(self):
		return self.product_name