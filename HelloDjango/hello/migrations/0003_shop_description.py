# Generated by Django 4.1.2 on 2023-03-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_products_image_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='description',
            field=models.CharField(default='description should be here', max_length=60),
        ),
    ]
