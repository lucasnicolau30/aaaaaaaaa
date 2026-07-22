from django.shortcuts import render
from products.models import Product
# from django.http import HttpResponse

# Create your views here.
# def product_view(request):
#     return HttpResponse("Hello, World!")

def product_view(request):
    # SELECT * FROM PRODUCTS;
    products = Product.objects.all()

    return render(
        request = request, 
        template_name = 'products.html',
        context = {
            'products': products
        }
    )