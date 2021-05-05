from django.shortcuts import render

# Create your views here.
def shipments(request):
	return render(request, 'shipment/shipment.html')
def add_shipment(request):
	return render(request, 'shipment/create_shipment.html')