from .manager import User

from django.db import models
from django.conf import settings
   
#Helper functions
def restaurant_path(instance, filename):
    return "restaurants/%s/%s" % (instance.name, filename)

#Shops & Products
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=restaurant_path, blank=True, null=True)
    banner = models.ImageField(default="/banner.jpeg", upload_to=restaurant_path, blank=True)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)  
    review_count = models.PositiveIntegerField(default=0)  # quick display like "⭐ 4.5 (200)"

    delivery_time = models.CharField(max_length=50, default="30-45 min")  # UX-friendly string
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    
    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="favorite_restaurants", blank=True
    )

    is_open = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.id} {self.name}"
    
#Products & Orders
class Category(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, related_name="categories", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.restaurant.name} - {self.name}"
        
class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.restaurant.name} selling {self.name}"
        

#Organize cart of orders on frontend
class Cart(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PAID = 'paid', 'Paid'
        SHIPPED = 'shipped', 'Shipped'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="carts")
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

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"Order {self.cart.id}: {self.quantity} x {self.product.name}"

# class OrderHistory(models.Model):

# class Category(models.Model):
#     name = models.CharField(
# 
# 
# 
# 
# 
# 
# 
# max_length=255)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="categories")