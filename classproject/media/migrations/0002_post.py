# Generated by Django 5.0.2 on 2024-03-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ImageField(upload_to='images/')),
                ('bio', models.CharField(max_length=200)),
            ],
        ),
    ]
