# Generated by Django 2.0.7 on 2018-07-06 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Additive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additive_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('risk', models.IntegerField(blank=True, choices=[(0, 'Sans risque'), (1, 'Avec modération'), (2, 'Douteux'), (3, 'A éviter'), (4, 'Toxique')], null=True)),
                ('max_permissible_dose', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'additif',
            },
        ),
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergen_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'allergène',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('hierarchy', models.ManyToManyField(to='allergen.Category')),
            ],
            options={
                'verbose_name': 'catégorie',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'ingrédient',
            },
        ),
        migrations.CreateModel(
            name='Nutriment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutriment_name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('daily_quantity_m', models.CharField(max_length=255)),
                ('daily_quantity_f', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NutrimentComposeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutriment_quantity', models.CharField(max_length=255)),
                ('nutriment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='allergen.Nutriment')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255, verbose_name='nom du produit')),
                ('image_url', models.URLField(verbose_name="lien de l'image")),
                ('url_off', models.URLField(verbose_name='lien openfoodfacts')),
                ('barcode', models.BigIntegerField(db_index=True, unique=True, verbose_name='code barre')),
                ('nutrition_grade', models.CharField(max_length=1, verbose_name='nutriscore')),
                ('quantity', models.CharField(max_length=255, verbose_name='quantité')),
                ('additives', models.ManyToManyField(to='allergen.Additive')),
                ('allergens', models.ManyToManyField(to='allergen.Allergen')),
                ('categories', models.ManyToManyField(to='allergen.Category')),
                ('ingredients', models.ManyToManyField(to='allergen.Ingredient')),
                ('nutriments', models.ManyToManyField(through='allergen.NutrimentComposeProduct', to='allergen.Nutriment')),
            ],
            options={
                'verbose_name': 'produit',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexe', models.CharField(choices=[('m', 'Homme'), ('f', 'Femme')], max_length=1)),
                ('height', models.IntegerField(verbose_name='taille')),
                ('weight', models.IntegerField(verbose_name='poids')),
                ('age', models.IntegerField(verbose_name='âge')),
                ('basal_metabolism', models.IntegerField(verbose_name='métabolisme basal')),
                ('allergens', models.ManyToManyField(to='allergen.Allergen')),
                ('ingredients', models.ManyToManyField(to='allergen.Ingredient')),
                ('products', models.ManyToManyField(to='allergen.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistoric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Historique de recherche',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='allergen.Product', verbose_name='produit original')),
                ('replacement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacement', to='allergen.Product', verbose_name='produit de substitution')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'Substitut',
            },
        ),
        migrations.CreateModel(
            name='Trace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_origin', models.CharField(max_length=255)),
                ('translated_name', models.CharField(max_length=255)),
                ('language', models.CharField(default='fr', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Vitamin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vitamin_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('daily_quantity_m', models.CharField(max_length=255)),
                ('daily_quantity_f', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'vitamine',
            },
        ),
        migrations.CreateModel(
            name='VitaminComposeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vitamin_quantity', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allergen.Product')),
                ('vitamin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='allergen.Vitamin')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='traces',
            field=models.ManyToManyField(to='allergen.Trace'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='substitutes',
            field=models.ManyToManyField(through='allergen.Substitute', to='allergen.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='traces',
            field=models.ManyToManyField(to='allergen.Trace'),
        ),
        migrations.AddField(
            model_name='product',
            name='vitamins',
            field=models.ManyToManyField(through='allergen.VitaminComposeProduct', to='allergen.Vitamin'),
        ),
        migrations.AddField(
            model_name='nutrimentcomposeproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allergen.Product'),
        ),
    ]