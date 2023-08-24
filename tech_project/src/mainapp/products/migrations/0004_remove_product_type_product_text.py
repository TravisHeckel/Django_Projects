# Generated by Django 4.1 on 2023-08-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AddField(
            model_name='product',
            name='text',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], default='', max_length=60),
        ),
    ]