# Generated by Django 5.0.6 on 2024-07-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_alter_categoria_options_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
