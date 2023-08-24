# Generated by Django 4.1 on 2023-08-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
                ('firstname', models.CharField(blank=True, default='', max_length=60)),
                ('lastname', models.TextField(blank=True, default='', max_length=60)),
                ('email', models.TextField(blank=True, default='', max_length=60)),
                ('username', models.TextField(blank=True, default='', max_length=60)),
            ],
        ),
    ]