from django.db import models

from customers.models import Customer
from products.models import Product

# Create your models here.
class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'Delete'))
    #different stages of a cart
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_REJECTED=4
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERED,"ORDER_DELIVERED"),
                   (ORDER_REJECTED,"ORDER_REJECTED")
                   )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')# since the cart is for a user with one to many field
    delete_status = models.IntegerField(default=LIVE)
    created_at = models.DateTimeField(
        auto_now_add=True)  # for the recording of date and time when the data is updated and created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:

        return "order-{}-{}".format(self.id,self.owner.name)


#for storing multiple cart items
class OrderedItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')



