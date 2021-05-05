from django.db import models
from inventory.models import Inventory

class PointOfSale(models.Model):

	inventory_ref = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventory_ref', null=True)
	quantity = models.DecimalField(max_digits=28, decimal_places= 5, default=0, null=True)


	def __str__(self):
		return self.inventory_ref.shipment_ref.product.product_name