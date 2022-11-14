from django.db import models


class Bookshop(models.Model):
    title = models.CharField('Название книги', max_length=40)
    author = models.CharField('Автор', max_length=40)
    price = models.FloatField('Цена')

    class Meta:
        db_table = 'Bookshop'
        #f

# Create your models here.
