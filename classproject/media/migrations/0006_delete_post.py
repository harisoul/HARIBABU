# Generated by Django 5.0.2 on 2024-03-22 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='post',
        ),
    ]