# Generated by Django 4.0.5 on 2022-06-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_alter_work_izo_alter_work_bio_alter_work_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='day',
            field=models.CharField(default='', max_length=50, verbose_name='День недели'),
        ),
    ]
