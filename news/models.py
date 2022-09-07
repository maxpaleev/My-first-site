from django.db import models
import time
from datetime import date

week = time.localtime()
time = week.tm_mday, week.tm_mon, week.tm_year


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField("Текст")
    date = models.DateField('Дата публикации', default=date.today(), max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Новость"
