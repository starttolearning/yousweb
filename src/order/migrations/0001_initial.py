# Generated by Django 2.1.2 on 2018-11-04 15:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(help_text='请务必仔细填写填，方便我们联系你。', max_length=200, verbose_name='联系人')),
                ('contact_phone', models.CharField(help_text='请务必填写正确。 填写11位的电话号码。', max_length=11, verbose_name='联系电话')),
                ('product', models.CharField(choices=[('广告', (('ad1', '喷绘'), ('ad2', '写真'))), ('打印', (('pt1', '论文修改'), ('pt2', '复习资料'))), ('other', '其他')], default='ad1', max_length=10)),
                ('description', models.TextField(blank=True, help_text='请添加你对产品设计制作和安装过程中的详细要求。', null=True, verbose_name='具体要求请备注')),
                ('status', models.IntegerField(choices=[(0, '等待处理'), (1, '前台已经接单'), (2, '设计师设计中...'), (3, '等待定稿...'), (4, '等待安装...'), (5, '正在配送安装...'), (6, '订单完成')], default=0, verbose_name='产品状态')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2018, 11, 4, 23, 41, 4, 674109), verbose_name='订单生成时间')),
                ('finish_time', models.DateTimeField(auto_now=True, verbose_name='finish date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
