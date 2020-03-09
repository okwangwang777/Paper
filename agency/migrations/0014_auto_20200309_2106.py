# Generated by Django 2.0 on 2020-03-09 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0013_auto_20200309_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packdocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=128, null=True, verbose_name='文档名称')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.Users', verbose_name='用户')),
            ],
            options={
                'verbose_name': '打包文档',
                'verbose_name_plural': '打包文档',
                'db_table': 'packdocument',
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='filename',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.CharField(default=0, max_length=16, verbose_name='时间'),
        ),
        migrations.AddField(
            model_name='order',
            name='ordernumber',
            field=models.CharField(default=0, max_length=20, verbose_name='订单号'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity_residual',
            field=models.IntegerField(default=0, verbose_name='剩余数量'),
        ),
    ]