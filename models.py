from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    details = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images')
   
   
    def __str__(self):
        return self.name
class Order(models.Model):
    # Your Order model fields go here
    # For example:
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    def __str__(self):
        return f"Order {self.pk}"