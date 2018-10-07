# _*_ coding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile


# Create your models here.

class Meeting(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"登陆名", null=True, blank=True)
    dishi = models.CharField(max_length=20, verbose_name=u"地市")
    name = models.CharField(max_length=20, verbose_name=u"参会人员")
    gender = models.CharField(max_length=6, choices=(('male', u"男"), ('female', u"女")), default="male")
    danwei = models.CharField(max_length=20, verbose_name=u"单位名称")
    address = models.CharField(max_length=100, default="", verbose_name=u"单位地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号")
    email = models.EmailField(verbose_name=u"邮箱",null=True, blank=True,default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"会议回执"
        verbose_name_plural = verbose_name

