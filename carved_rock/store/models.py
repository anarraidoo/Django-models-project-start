from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField(help_text="How many items are currently in stock")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)

    '''
    Add a field called "sku"
    This is a unique code for each product
    it is a string of maximum 20 characters long
    field label in the admin says "stock keeping unit" instead of "sku"
    '''
    sku = models.CharField(max_length=20, verbose_name="stock keeping unit", unique=True)

    class Meta:
        ordering = ['price']
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return self.name
