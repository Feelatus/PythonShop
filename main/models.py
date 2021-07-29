from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  name = models.CharField(max_length=200, db_index=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to='images/', blank=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'Product'
    verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class SliderHome(models.Model):
  name = models.CharField(max_length=200, db_index=True)
  image = models.ImageField(upload_to='slides/', blank=True)
  description = models.TextField(blank=True)
  link = models.TextField(max_length = 200)

  class Meta:
    ordering = ('name',)
    verbose_name = 'SliderHome'
    verbose_name_plural = 'SlidersHome'
      
    def __str__(self):
        return self.name

class SliderAdd(models.Model):
  name = models.CharField(max_length=200, db_index=True)
  image = models.ImageField(upload_to='slides_add/', blank=True)
  description = models.TextField(blank=True)
  link = models.URLField(max_length = 200)

  class Meta:
    ordering = ('name',)
    verbose_name = 'SliderAdd'
    verbose_name_plural = 'SlidersAdd'
      
    def __str__(self):
        return self.name
