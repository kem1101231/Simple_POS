from django.shortcuts import render

def point_of_sale_home(request):
	return render(request, 'point_of_sale/point_of_sale.html')