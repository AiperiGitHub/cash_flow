# Generated by Django 4.2 on 2023-04-24 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='TransactionImage',
        ),
    ]
