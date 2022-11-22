from django.db import models


class Bookshop(models.Model):
    title = models.CharField('Название книги', max_length=40)
    author = models.CharField('Автор', max_length=40)
    price = models.FloatField('Цена')

    class Meta:
        db_table = 'Bookshop'


class Users(models.Model):
    login = models.CharField(max_length=255, blank=False, default='')
    password = models.CharField(max_length=128, blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    name = models.CharField(max_length=255, blank=False, default='')
    role = models.CharField(max_length=255, blank=False, default='')

    #def save(self, *args, **kwargs):
    #self.password = make_password(self.password)
    #super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = 'users'

# Create your models here.
