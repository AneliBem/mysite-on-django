from django.db import models


# product on computer shop
class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='items_product')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_length=20, decimal_places=2)
    discount = models.DecimalField(max_length=5, decimal_places=2)
    warranty = models.PositiveSmallIntegerField(default=12)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

    def get_price_with_discount(self):
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100))
        return self.price
    

