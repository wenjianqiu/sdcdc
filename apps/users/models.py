# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# 自定一个表，覆盖原始的user表
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="",null=True, blank=True)
    birthday = models.DateField(verbose_name=u"出生日期", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', u"男"), ('female', u"女")), default="female",null=True, blank=True)
    address = models.CharField(max_length=100, default="",null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default",null=True, blank=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username




