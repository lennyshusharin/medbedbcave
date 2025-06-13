from django.db import models

class Product(models.Model):
    type = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    store_article = models.CharField(max_length=50, blank=True, null=True)
    supplier_article = models.CharField(max_length=50, blank=True, null=True)

    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity_received = models.PositiveIntegerField(default=0)
    quantity_sold = models.PositiveIntegerField(default=0)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} {self.size} ({self.color})"


class Supply(models.Model):
    date = models.DateField()
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Поставка {self.date}"


class SupplyItem(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.product} x{self.quantity}"


class Sale(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Продаж {self.date}"


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} x{self.quantity} продано"