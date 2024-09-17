# Generated by Django 5.1.1 on 2024-09-07 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Name')),
                ('E_mail', models.EmailField(max_length=254, verbose_name='E_Mail')),
                ('Number', models.IntegerField(verbose_name='Phone Number')),
                ('Description', models.TextField(max_length=200, verbose_name='Your message Request')),
            ],
        ),
    ]
