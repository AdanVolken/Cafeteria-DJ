# Generated by Django 4.2.7 on 2023-11-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_bebida_ingredientes_alter_comida_ingredientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='bebida',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='bebida/imagen'),
        ),
        migrations.AddField(
            model_name='comida',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='comida/imagen'),
        ),
    ]