# Generated by Django 3.2.4 on 2021-06-12 17:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0001_author_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('phone_number', models.CharField(help_text='Start the province code, like 02100000000', max_length=11, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number.', regex='^0[0-9]{2,}[0-9]{7,}$')], verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
        ),
    ]
