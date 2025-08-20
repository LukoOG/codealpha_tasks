from .manager import User

from django.db import models
    
#Shops & Products
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="restaurants/", blank=True, null=True)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} {self.name}"
    
#Products & Orders
class Product(models.Model):
    # class Category(models.TextChoices):
    #     Pizza = "pizza", "Pizza"
    #     Drink = "drink", "Drink"

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) #Price in dollars


    def __str__(self):
        return f"{self.restaurant.name} selling {self.name}"

#Organize cart of orders on frontend
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PAID = 'paid', 'Paid'
        SHIPPED = 'shipped', 'Shipped'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(
        max_length=20,
        choices=Status,
        default=Status.PENDING
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"Order {self.order.id}: {self.quantity} x {self.product.name}"

# class OrderHistory(models.Model):

# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="categories")