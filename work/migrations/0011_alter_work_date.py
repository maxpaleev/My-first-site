# Generated by Django 4.0.5 on 2022-06-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0010_alter_work_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(default=(2, 6, 2022), verbose_name='Дата'),
        ),
    ]
