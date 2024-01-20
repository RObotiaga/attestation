from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода')

    def __str__(self):
        return f'{self.name} {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Supplier(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Название')
    type = models.CharField(choices=[('factory', 'Завод'),
                                     ('RetailNetwork', 'Розничная сеть'),
                                     ('IndividualEntrepreneur', 'ИП')],
                            default='factory',
                            verbose_name='Тип звена')
    email = models.EmailField()
    country = models.CharField(max_length=255,
                               verbose_name='Страна')
    city = models.CharField(max_length=255,
                            verbose_name='Город')
    street = models.CharField(max_length=255,
                              verbose_name='Улица')
    house_number = models.CharField(max_length=10,
                                    verbose_name='Номер строения')
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    supplier = models.ForeignKey('self',
                                 null=True, blank=True,
                                 on_delete=models.CASCADE,
                                 related_name='child_suppliers',
                                 verbose_name='Поставщики')
    debt_to_supplier = models.DecimalField(max_digits=13,
                                           decimal_places=2,
                                           default=0,
                                           null=True, blank=True,
                                           verbose_name='Задолженность')
    creation_time = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
