# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-25 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category1', models.CharField(max_length=20, verbose_name='男士/女士')),
                ('category2', models.CharField(max_length=20, verbose_name='季节')),
            ],
        ),
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('waresname', models.CharField(max_length=30, verbose_name='商品名字')),
                ('waresinfo', models.CharField(max_length=200, verbose_name='商品详情')),
                ('waressize', models.CharField(max_length=4,verbose_name='商品尺码')),
                ('waresstock', models.PositiveIntegerField(default=0, verbose_name='商品库存')),
                ('warescount', models.PositiveIntegerField(default=0, verbose_name='商品销量')),
                ('waresprice', models.FloatField(max_length=7, verbose_name='商品价格')),
                ('borntime', models.DateTimeField(auto_now_add=True, verbose_name='上架时间')),
                ('warestatus', models.BooleanField(default=True, verbose_name='商品状态')),
                ('forgoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.stores')),
            ],
        ),
        migrations.CreateModel(
            name='goodsimgs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imag0', models.ImageField(upload_to='static/upload/goods', verbose_name='商品图片')),
                ('forimg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='forcat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods'),
        ),
    ]