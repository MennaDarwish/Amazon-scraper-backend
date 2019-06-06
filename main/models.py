from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    rank = models.CharField(max_length=255, null=True, blank=True)
    product_dimensions = models.CharField(max_length=255,
                                          null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    sale_price = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    asin = models.CharField(primary_key=True, max_length=255,
                            null=False, blank=False)
    image = models.CharField(max_length=516, null=True, blank=True)
    rank = models.CharField(max_length=516, null=True, blank=True)

    def __str__(self):
        return self.name
