# Generated by Django 4.1.2 on 2022-12-02 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_alter_shop_owner_delete_owners'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='owner',
            new_name='ownerProfile',
        ),
    ]
