import time

from django.db import models

week = time.localtime()

if week.tm_wday == 0:
    day = 'Понедельник'
elif week.tm_wday == 1:
    day = 'Вторник'
elif week.tm_wday == 2:
    day = 'Среда'
elif week.tm_wday == 3:
    day = 'Четверг'
elif week.tm_wday == 4:
    day = 'Пятница'
elif week.tm_wday == 5:
    day = 'Суббота'

time = week.tm_wday, week.tm_mon, week.tm_year


class Work(models.Model):
    day = models.CharField('День недели', max_length=50, default=day, null=True, blank=True)
    rus = models.CharField('Русский', max_length=50, null=True, blank=True)
    match = models.CharField('Математика', max_length=50, null=True, blank=True)
    lit = models.CharField('Лит-ра', max_length=50, null=True, blank=True)
    bio = models.CharField('Биология', max_length=50, null=True, blank=True)
    eng = models.CharField('Английский', max_length=50, null=True, blank=True)
    IZO = models.CharField('Изо', max_length=50, null=True, blank=True)
    inf = models.CharField('Информатика', max_length=50, null=True, blank=True)
    geo = models.CharField('География', max_length=50, null=True, blank=True)
    his = models.CharField('История', max_length=50, null=True, blank=True)
    science = models.CharField('Общество', max_length=50, null=True, blank=True)
    teh = models.CharField('Технология', max_length=50, null=True, blank=True)
    deutsch = models.CharField('Немецкий', max_length=50, null=True, blank=True)
    date = models.CharField('Дата', max_length=50, null=True, blank=True, default=time)

    def __str__(self):
        return f'День:{self.day}'

    def get_absolute_url(self):
        return f'/homework/{self.id}'

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашнии задания'
