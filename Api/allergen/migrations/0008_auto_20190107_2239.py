# Generated by Django 2.1.4 on 2019-01-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergen', '0007_nutriment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='basal_metabolism',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sexe',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='weight',
        ),
        migrations.AlterField(
            model_name='profile',
            name='allergens',
            field=models.ManyToManyField(blank=True, to='allergen.Allergen'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='allergen.Ingredient'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='products',
            field=models.ManyToManyField(blank=True, to='allergen.Product'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='traces',
            field=models.ManyToManyField(blank=True, to='allergen.Trace'),
        ),
    ]