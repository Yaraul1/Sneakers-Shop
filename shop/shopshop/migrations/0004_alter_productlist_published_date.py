# Generated by Django 4.0.5 on 2022-07-12 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopshop', '0003_alter_productlist_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 12, 22, 41, 50, 481397), null=True, verbose_name='Дата публикации'),
        ),
    ]
