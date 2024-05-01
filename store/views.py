from django.shortcuts import render, get_object_or_404
from store.models import Product

def store(request):
    products = Product.objects.filter(is_available=True)
    products_count = products.count()
    context = {
        'products': products,
        'products_count': products_count
    }
    return render(request, 'store/store.html', context)



def show_product_detail_by_name(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, is_available=True)
    context = {
        'product': product
    }
    return render(request, 'store/product-detail.html', context)