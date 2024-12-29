# Generated by Django 5.1.4 on 2024-12-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('code', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
