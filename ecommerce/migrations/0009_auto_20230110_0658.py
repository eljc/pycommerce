# Generated by Django 3.2 on 2023-01-10 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_rename_recived_order_received'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]