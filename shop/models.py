from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    