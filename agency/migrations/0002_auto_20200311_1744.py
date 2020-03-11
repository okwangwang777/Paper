# Generated by Django 2.0 on 2020-03-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectionlist',
            name='detection_number',
            field=models.CharField(default='', max_length=33, verbose_name='前端查询编号'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(default=2, max_length=16, verbose_name='实付金额'),
            preserve_default=False,
        ),
    ]