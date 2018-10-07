# _*_ encoding:utf-8 _*_
__date__ = "2018/10/4 18:40"


import xadmin
from xadmin import views



# 修改全局界面设置
# class BaseSetting(object):

    # enable_themes = True
    # use_bootswatch = True

class GlobalSetting(object):
    site_title = "信息收集系统"
    site_footer = "山东省疾控中心病毒所"
    #设置菜单是否可以收缩合并
    # menu_style = "accordion"


# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


