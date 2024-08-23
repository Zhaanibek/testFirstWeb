from django.db import models
from django.urls import reverse


class CategoryRental(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category_rental'
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории - Аренда'

    def __str__(self):
        return self.name
    

class CategorySpare(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category_spare'
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории - Запчасти'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='cars_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name} - количество {self.quantity}'
    
    def get_absolute_url(self):
        return reverse(f"catalog:{self.__class__.__name__.lower()}", kwargs={"product_slug": self.slug})
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        return self.price
    

class ProductCarRental(Product):
    in_stock = models.BooleanField(default=False, verbose_name='В наличии')
    category = models.ForeignKey(to='CategoryRental', on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'productCarRental'
        verbose_name = 'Машина в аренду'
        verbose_name_plural = 'Машины в аренду'
        ordering = ('id',)


class ProductSpare(Product):
    category = models.ForeignKey(to='CategorySpare', on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'productSpare'
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'
        ordering = ('id',)
