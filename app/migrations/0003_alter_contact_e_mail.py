# Generated by Django 5.1.1 on 2024-09-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='E_mail',
            field=models.EmailField(max_length=254, verbose_name='E-Mail'),
        ),
    ]
