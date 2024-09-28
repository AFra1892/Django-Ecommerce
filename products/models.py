from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now=True)
    # modified_at
    # deleted_at

    def __str__(self):
        return self.name



class Discount(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True , null=True)
    discount_percent = models.FloatField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    # modified_at
    # deleted_at

    def __str__(self):
        return str(self.discount_percent)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True , null=True)
    category = models.ForeignKey(Category  , on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    inventory = models.IntegerField(null=True)
    discount_id = models.ForeignKey(Discount  ,blank=True,null=True,  on_delete=models.CASCADE) 
    # modified_at
    # deleted_at
    # SKU
    def __str__(self):
        return f"{self.name} - {self.category}"
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})
    
# class Inventory(models.Model):
#     product = models.OneToOneField(Product,null=True, on_delete=models.CASCADE, related_name='inventory')
#     quantity = models.IntegerField()
#     created_at = models.DateTimeField(auto_now=True)
#     # modified_at
#     # deleted_at

#     def __str__(self):
#         return str(self.quantity)  

    
