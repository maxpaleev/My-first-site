# Generated by Django 4.0.5 on 2022-06-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_work_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='lit',
            field=models.CharField(max_length=50, verbose_name='Лит-ра'),
        ),
        migrations.AlterField(
            model_name='work',
            name='match',
            field=models.CharField(max_length=50, verbose_name='Математика'),
        ),
        migrations.AlterField(
            model_name='work',
            name='rus',
            field=models.CharField(max_length=50, verbose_name='Русский'),
        ),
    ]
