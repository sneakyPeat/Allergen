# Generated by Django 2.0.7 on 2018-07-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergen', '0002_auto_20180711_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrimentcomposeproduct',
            name='nutriment_quantity',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
    ]
