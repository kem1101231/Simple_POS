from django.db import models
from shipment.models import ShipmentLines,Shipment

class Inventory(models.Model):

	shipment_ref = models.ForeignKey(ShipmentLines, on_delete=models.CASCADE, related_name='shipment_ref', null=True)
	batch_number = models.IntegerField(null=True)
	available = models.DecimalField(max_digits=28, decimal_places= 5, default=0, null=True)
	selling_price = models.DecimalField(max_digits=28, decimal_places= 5, default=0, null=True)


	def __str__(self):
		return self.shipment_ref.shipment_code +"-"+ self.shipment_ref.product.product_name