# Generated by Django 4.0.5 on 2022-06-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0012_alter_work_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='deutsch',
            field=models.CharField(default='не задано ', max_length=50, verbose_name='Немецкий'),
        ),
        migrations.AddField(
            model_name='work',
            name='teh',
            field=models.CharField(default='не задано ', max_length=50, verbose_name='Технология'),
        ),
    ]
