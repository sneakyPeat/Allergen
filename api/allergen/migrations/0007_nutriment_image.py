# Generated by Django 2.1.2 on 2018-10-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergen', '0006_remove_product_translations'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutriment',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]