from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from store.models import Product
from .models import Order, OrderItem
from django.contrib import messages
import time


def cart(request):
    select_user_order_main_basket = Order.objects.filter(user=request.user.pk, is_complete=False).first()
    order_items = OrderItem.objects.filter(order=select_user_order_main_basket).all()
    try:
        order_total_price = select_user_order_main_basket.calculate_total_price()
        tax = (0.02 * float(order_total_price))
        price_with_tax = float(order_total_price) + tax
    except Exception:
        order_total_price = None
        tax = None
        price_with_tax = None
    context = {
        'order_items': order_items,
        "order_total_price": order_total_price,
        "tax": tax,
        "price_with_tax": price_with_tax,

    }
    return render(request, 'carts/cart.html', context)


def add_product_to_basket(request):
    product_id = request.POST.get('product_id')
    size = request.POST.get('size')
    color = request.POST.get('color')
    product_exists = get_object_or_404(Product, id=product_id)
    has_open_basket = Order.objects.filter(user=request.user.pk, is_complete=False).first()
    if has_open_basket:
        already_purchased_this_item = OrderItem.objects.filter(product=product_exists, color=color, size=size).first()
        if already_purchased_this_item:
            already_purchased_this_item.quantity += 1
            already_purchased_this_item.save()
        else:
            OrderItem.objects.create(product=product_exists,
                                     order=has_open_basket,
                                     price=product_exists.price,
                                     color=color,
                                     size=size)
    else:
        new_basket = Order.objects.create(user=request.user)
        OrderItem.objects.create(product=product_exists,
                                 order=new_basket,
                                 price=product_exists.price,
                                 color=color,
                                 size=size)
    messages.success(request, "Product added to your basket successfully.")
    time.sleep(20)
    return redirect(reverse("product-detail-page", kwargs={"product_slug": product_exists.slug}))


def remove_product_from_basket(request, product_slug):
    select_user_open_basket = Order.objects.filter(user=request.user.pk, is_complete=False).first()
    is_product_exsits_in_user_basket = OrderItem.objects.filter(order=select_user_open_basket,
                                                                product__slug=product_slug).first()
    if is_product_exsits_in_user_basket:
        is_product_exsits_in_user_basket.delete()
    return redirect(reverse("cart-page"))


def increase_product_quantity(request, product_slug):
    select_user_open_basket = Order.objects.filter(user=request.user.pk, is_complete=False).first()
    is_product_exsits_in_user_basket = OrderItem.objects.filter(order=select_user_open_basket,
                                                                product__slug=product_slug).first()
    if is_product_exsits_in_user_basket:
        is_product_exsits_in_user_basket.quantity += 1
        is_product_exsits_in_user_basket.save()
    return redirect(reverse("cart-page"))


def decrease_product_quantity(request, product_slug):
    select_user_open_basket = Order.objects.filter(user=request.user.pk, is_complete=False).first()
    is_product_exsits_in_user_basket = OrderItem.objects.filter(order=select_user_open_basket,
                                                                product__slug=product_slug).first()
    if is_product_exsits_in_user_basket:
        is_product_exsits_in_user_basket.quantity -= 1
        if is_product_exsits_in_user_basket.quantity < 1:
            is_product_exsits_in_user_basket.delete()
            return redirect(reverse("cart-page"))
        is_product_exsits_in_user_basket.save()
    return redirect(reverse("cart-page"))


def show_user_basket(request):
    select_user_order_main_basket = Order.objects.filter(user=request.user.pk, is_complete=False).first()
    order_items = OrderItem.objects.filter(order=select_user_order_main_basket).all()
    return order_items
