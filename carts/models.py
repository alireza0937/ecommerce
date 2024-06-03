from django.db import models
from user.models import User
from store.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = 'Orders'
        db_table = 'Orders'
        
    def __str__(self):
        return str(self.user)
    
    
    def calculate_total_price(self):
        total_price = 0
        for order_item in self.orderitem_set.all():
            total_price += order_item.calculate_each_product_total_price()
        self.total_price = total_price
        return self.total_price
    
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    
    class Meta:
        verbose_name_plural = 'OrderItems'
        db_table = 'OrderItems'
        
    def __str__(self) -> str:
        return self.product.name
    
    
    def calculate_each_product_total_price(self):
        total_price = self.price * self.quantity
        return total_price