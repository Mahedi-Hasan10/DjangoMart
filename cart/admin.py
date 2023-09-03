from django.contrib import admin

# Register your models here.
from .models import Cart,CartItem
class CartItemModel(admin.ModelAdmin):
    list_display =['product','user','cart','quantity','is_active','sub_total']
admin.site.register(Cart)
admin.site.register(CartItem,CartItemModel)