# Generated by Django 3.1.4 on 2021-07-29 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_slideradd_sliderhome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slideradd',
            options={'ordering': ('name',), 'verbose_name': 'SliderAdd', 'verbose_name_plural': 'SlidersAdd'},
        ),
        migrations.AlterModelOptions(
            name='sliderhome',
            options={'ordering': ('name',), 'verbose_name': 'SliderHome', 'verbose_name_plural': 'SlidersHome'},
        ),
    ]