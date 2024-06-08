from django.shortcuts import get_object_or_404, render
from category.models import Category
from store.models import Product


def header_components(request):
    return render(request, 'share/header.html')


def footer_components(request):
    return render(request, 'share/footer.html')


def index(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)


def show_product_by_category(request, category_slug):
    products = Product.objects.filter(category__slug=category_slug, is_available=True).prefetch_related('category')
    get_object_or_404(Category, slug=category_slug)
    context = {
        'products': products,
        "products_count": products.count(),
    }
    return render(request, 'store/store.html', context)
