# Generated by Django 4.0 on 2022-11-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=500)),
                ('level_one', models.CharField(max_length=100)),
                ('level_two', models.CharField(max_length=100)),
                ('level_three', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('alt_price', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=100)),
                ('property_fields', models.CharField(max_length=100)),
                ('joint_purchases', models.CharField(max_length=100)),
                ('measure_unit', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=1000)),
                ('display_on_index', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
