from django.db import models

units = [
    ('kg', 'kg'),
    ('l', 'l'),
    ('ml', 'ml'),
    ('mg', 'mg'),
    ('g', 'g'),
]

class Products(models.Model):
    name = models.CharField(max_length=12)
    price = models.IntegerField()
    unit = models.CharField(choices=units, max_length=2)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Categories(models.Model):
    name = models.CharField(max_length=13)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
