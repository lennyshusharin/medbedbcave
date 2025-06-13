from django.contrib import admin
from .models import Product, Supply, SupplyItem, Sale, SaleItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "size", "color", "entry_price", "retail_price", "quantity_in_stock")
    search_fields = ("brand", "model", "color", "store_article", "supplier_article")
    list_filter = ("type", "brand", "color")


class SupplyItemInline(admin.TabularInline):
    model = SupplyItem
    extra = 1


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ("date", "delivery_cost")
    inlines = [SupplyItemInline]


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("date", "channel")
    inlines = [SaleItemInline]