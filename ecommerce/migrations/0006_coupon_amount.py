# Generated by Django 3.2 on 2023-01-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_order_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]