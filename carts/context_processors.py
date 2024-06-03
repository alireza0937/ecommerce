from carts.models import Order, OrderItem


def show_amount_of_items_in_basket(request):
    has_open_basket = Order.objects.filter(user=request.user.pk, is_complete=False).first()
    if has_open_basket:
        items_in_basket = OrderItem.objects.filter(order=has_open_basket).count()
    else:
        items_in_basket = 0
    return dict(links2=items_in_basket)