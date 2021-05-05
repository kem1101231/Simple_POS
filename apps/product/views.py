from django.shortcuts import render

# Create your views here.
def product_list(request):
	return render(request, 'product/products.html')

def add_product(request):
	return render(request, 'product/create_product.html')