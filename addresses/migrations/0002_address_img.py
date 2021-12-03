# Generated by Django 3.2.9 on 2021-11-11 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/%y/%m/%d'),
            preserve_default=False,
        ),
    ]