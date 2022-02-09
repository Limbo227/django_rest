from django.db import models
from django.contrib.auth import get_user_model


class House(models.Model):
    User = get_user_model()
    reg_number = models.CharField('Регистрационный номер',
                                  db_index=True,
                                  unique=True,
                                  max_length=10)
    area = models.CharField('Площадь',
                            max_length=6,)
    HOUSE_TYPES = (
        (1, 'Монсардный'),
        (2, 'Частный'),
        (3, 'Балконские'),
        (4, 'Элитки'),
        (5, 'Тауехаус'),
        (6, 'Пентхаус'),)
    types = models.CharField(
        'Тип дома',
        choices=HOUSE_TYPES, max_length=50
    )
    builder = models.CharField('Подрядчик', max_length=60,)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)

class Tegy(models.Model):
    title = models.CharField('Теги', max_length=25)

    def __str__(self):
        return self.title

