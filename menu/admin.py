from django.contrib import admin

from menu.models import Product

# Register your models here.
# admin.site.register(Product)


@admin.register(Product)
class EcoProductAdmin(admin.ModelAdmin):
    # list display
    list_display = ['item_name', 'item_price', 'item_category', 'item_in_stock']
    # list Filter
    list_filter = ['item_category', 'item_in_stock']
    # search list
    search_fields = ['item_name']
