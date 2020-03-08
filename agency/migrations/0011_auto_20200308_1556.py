# Generated by Django 2.0 on 2020-03-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_auto_20200303_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Globo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='名称')),
                ('info', models.CharField(max_length=128, verbose_name='信息')),
            ],
            options={
                'verbose_name': '全局管理',
                'verbose_name_plural': '全局管理',
                'db_table': 'globo',
            },
        ),
        migrations.AlterModelOptions(
            name='isactivatecode',
            options={'verbose_name': '检测卡', 'verbose_name_plural': '检测卡'},
        ),
        migrations.AlterModelOptions(
            name='surplus',
            options={'verbose_name': '代理充值', 'verbose_name_plural': '代理充值'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '代理列表', 'verbose_name_plural': '代理列表'},
        ),
        migrations.RemoveField(
            model_name='detectionlist',
            name='htmlurl',
        ),
        migrations.AddField(
            model_name='detectionlist',
            name='textnumber',
            field=models.IntegerField(default=0, verbose_name='文章字符数'),
        ),
        migrations.AlterField(
            model_name='detectionlist',
            name='iscode',
            field=models.IntegerField(blank=True, default=-2, null=True, verbose_name='状态'),
        ),
    ]
