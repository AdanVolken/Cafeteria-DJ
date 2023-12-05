# Generated by Django 4.2.3 on 2023-11-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ingredientes', models.TextField()),
                ('precio', models.IntegerField()),
                ('alcohol', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ingredientes', models.TextField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
