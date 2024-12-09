
# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Product  # Import the Product model



# def index(request):
#    products=Product.get_all_products();
#    print(products)
#    return render(request , 'index.html' , {'products':products})


from django.shortcuts import render
from .models import Product

def index(request):
    # Retrieve all products using the Django ORM
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
