# Generated by Django 3.1.2 on 2020-12-12 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201212_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='expire_date',
        ),
    ]
