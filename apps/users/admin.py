# _*_ encoding:utf-8 _*_
__date__ = "2018/10/4 21:44"
from django.contrib import admin

# Register your models here.


from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    # 设置下面的属性使显示时，输入后才加载该外键

    relfield_style = 'fk_ajax'
    pass


admin.site.register(UserProfile, UserProfileAdmin)
