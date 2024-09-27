from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return self.title
