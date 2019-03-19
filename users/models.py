from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import hashlib


# Create your models here.
class Cargo_Cards(models.Model):  # 该类与数据库同步的时候会创建该表，如果使用之前的库和表，class 后就写数据库中你想要用的表
    Cargo_Name = models.CharField(max_length=30,verbose_name='Cargo_Name')
    Quantity = models.CharField(max_length=50,verbose_name='Quantity')
    Loading_Port = models.CharField(max_length=60,verbose_name='Loading_Port')
    Discharging_Port = models.CharField(max_length=30,verbose_name='Discharging_Port')
    LayCan = models.CharField(max_length=50,verbose_name='LayCan')
    Sent = models.CharField(max_length=50,verbose_name='Sent')


def __unicode__(self):
    return self.name


class TC_Cards(models.Model):  # 该类与数据库同步的时候会创建该表，如果使用之前的库和表，class 后就写数据库中你想要用的表
    Account = models.CharField(max_length=30,verbose_name='Account')
    Quantity = models.CharField(max_length=50,verbose_name='Quantity')
    Delivery_Area = models.CharField(max_length=60,verbose_name='Delivery_Area')
    Redelivery_Area = models.CharField(max_length=30,verbose_name='Redelivery_Area')
    LayCan = models.CharField(max_length=50,verbose_name='LayCan')
    DUR = models.CharField(max_length=50,verbose_name='DUR')
    Sent = models.CharField(max_length=50,verbose_name='Sent')

class Tonnage_Cards(models.Model):  # 该类与数据库同步的时候会创建该表，如果使用之前的库和表，class 后就写数据库中你想要用的表
    Vessel_Name = models.CharField(max_length=30,verbose_name='Vessel_Name')
    DWT = models.CharField(max_length=10,verbose_name='DWT')
    BLT = models.IntegerField(max_length=60,verbose_name='BLT')
    Open_Area = models.CharField(max_length=30,verbose_name='Open_Area')
    Open_Date = models.CharField(max_length=50,verbose_name='Open_Date')
    Sent = models.CharField(max_length=50,verbose_name='Sent')
