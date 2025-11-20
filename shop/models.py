from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)   
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def add_stock(self, amount: int) -> None:
        if amount <= 0:
            print(f"{amount} is not a valid amount.")
            return
        self.quantity += amount
        self.save()
    
    def remove_stock(self, amount: int) -> None:
        if self.quantity - amount < 0:
            print(f"{amount} is not a valid amount.")
            return
        self.quantity -= amount
        self.save()

    def is_in_stock(self) -> bool:
        return self.quantity > 0
    
    def __str__(self) -> str:
        return f"{self.product.name} - {self.quantity} in stock."

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.total_price()
        return total
    
    def add_item(self):
        pass

    def remove_item(self):
        pass

    def clear_cart(self):
        pass

    def __str__(self):
        return f"Cart"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")

    def total_price(self):
        # No taxes 😁
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product} - {self.quantity}"


    