# Generated by Django 3.2.12 on 2022-03-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
