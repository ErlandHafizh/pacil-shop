# Generated by Django 5.1.1 on 2024-09-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sections',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
