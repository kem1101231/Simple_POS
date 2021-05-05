from django.db import models
from product.models import Unit,Product

class Supplier(models.Model):
	supplier_name = models.CharField(max_length=50)
	supplier_address = models.CharField(max_length=255)
	
	def __str__(self):
		return self.supplier_name

class ShipmentLines(models.Model):

	shipment_code = models.CharField(max_length=50)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True)
	quantity = models.DecimalField(max_digits=28, decimal_places= 5, default=0, null=True)
	unit_price = models.DecimalField(max_digits=28, decimal_places= 5, default=0, null=True)


class Shipment(models.Model):

	shipment_code = models.CharField(max_length=50)
	or_number = models.CharField(max_length=50)
	or_date = models.DateField()
	or_amount_total = models.DecimalField(max_digits=28, decimal_places= 5, default=0, null=True)

	shipment_items = models.ManyToManyField(ShipmentLines)

	def __str__(self):
		return self.shipment_code