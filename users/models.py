
from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import hashlib
from datetime import date


# Create your models here.
class Cargo_Card(models.Model):  # 该类与数据库同步的时候会创建该表，如果使用之前的库和表，class 后就写数据库中你想要用的表
    Cargo_name = models.CharField(max_length=30, verbose_name='Cargo_name')
    Quantity = models.CharField(max_length=50, verbose_name='Quantity')
    Loading_Port = models.CharField(max_length=60, verbose_name='Loading_Port')
    Discharging_Port = models.CharField(max_length=30, verbose_name='Discharging_Port')
    LayCan_S = models.DateField(default=date(1900, 1, 1), verbose_name='LayCan_S')
    LayCan_E = models.DateField(default=date(1900, 1, 1), verbose_name='LayCan_E')
    Sent = models.CharField(max_length=50, verbose_name='Sent')
    ID = models.IntegerField(max_length=11, verbose_name='ID', primary_key=True)
    mail_text = models.TextField(verbose_name='mail_text')

    class Meta:
        db_table = "cargo_card"


def __unicode__(self):
    return self.name


class TC_Card(models.Model):  # 该类与数据库同步的时候会创建该表，如果使用之前的库和表，class 后就写数据库中你想要用的表
    Account = models.CharField(max_length=30, verbose_name='Account')
    Quantity = models.CharField(max_length=50, verbose_name='Quantity')
    Delivery_area = models.CharField(max_length=60, verbose_name='Delivery_area')
    Redelivery_area = models.CharField(max_length=30, verbose_name='Redelivery_area')
    LayCan_E = models.DateField(default=date(1900, 1, 1), verbose_name='LayCan_E')
    LayCan_S = models.DateField(default=date(1900, 1, 1), verbose_name='LayCan_S')
    DUR = models.CharField(max_length=50, verbose_name='DUR')
    Sent = models.CharField(max_length=50, verbose_name='Sent')
    ID = models.IntegerField(max_length=11, verbose_name='ID', primary_key=True)
    mail_text = models.TextField(verbose_name='mail_text')

    class Meta:
        db_table = "tc_card"


class Tonnage_Card(models.Model):  # 该类与数据库同步的时候会创建该表，如果使用之前的库和表，class 后就写数据库中你想要用的表
    Vessel_name = models.CharField(max_length=30, verbose_name='Vessel_name')
    DWT = models.IntegerField(max_length=10, verbose_name='DWT')
    BLT = models.IntegerField(max_length=60, verbose_name='BLT')
    Open_area = models.CharField(max_length=30, verbose_name='Open_area')
    Open_date_S = models.DateField(default=date(1900, 1, 1), max_length=50, verbose_name='Open_date_S')
    Open_date_E = models.DateField(default=date(1900, 1, 1), max_length=50, verbose_name='Open_date_E')
    Sent = models.CharField(max_length=50, verbose_name='Sent')
    ID = models.IntegerField(max_length=11, verbose_name='ID', primary_key=True)
    mail_text = models.TextField(verbose_name='mail_text')

    class Meta:
        db_table = "tonnage_card"