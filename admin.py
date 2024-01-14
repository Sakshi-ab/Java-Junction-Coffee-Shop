from django.contrib import admin
from javajunctionapp.models import product, Order

# Register your models here.
class productName(admin.ModelAdmin):
    list_display =['id','name','price','details','category']
admin.site.register(product,productName)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'total_price', 'status']

admin.site.register(Order, OrderAdmin)