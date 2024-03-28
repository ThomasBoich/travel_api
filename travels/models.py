from django.db import models
from users.models import CustomUser
# Create your models here.

class Travel(models.Model):
    city = models.CharField(max_length=200, verbose_name='Город, Курорт', blank=True, null=True)
    country = models.ManyToManyField('Country', related_name= 'travels', verbose_name='Страна', blank=True, null=True)
    days = models.IntegerField(verbose_name='Количество дней', blank=True, null=True)
    date = models.DateField(verbose_name='Когда', blank=True, null=True)
    description = models.TextField(verbose_name='Описание путешествия', blank=True, null=True)
    travel_now = models.BooleanField(default=False, verbose_name='Уже путешествую', blank=True, null=True)


class Country(models.Model):
    name = models.CharField(max_length=200, verbose_name='Страна', blank=True, null=True)
    image = models.ImageField(upload_to='countries/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'