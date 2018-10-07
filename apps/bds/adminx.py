# _*_ encoding:utf-8 _*_

from xadmin.layout import Main, Fieldset, Row, Side
from xadmin.plugins.utils import get_context_dict

__date__ = "2018/10/4 21:44"

from import_export import resources
from django.template import loader

import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView

from .models import Meeting


class MeetingResource(resources.ModelResource):
    class Meta:
        model = Meeting
        # import_id_fields = {}
        # fields = ()
        # exclude = ('user',)


@xadmin.sites.register(Meeting)
class MeetingAdmin(object):
    import_export_args = {'import_resource_class': MeetingResource, 'export_resource_class': MeetingResource}

    list_display = ['id', 'name', 'gender', 'danwei', 'dishi', 'mobile', 'email']
    search_fields = ['name', 'gender', 'danwei', 'dishi']
    list_filter = ['name', 'gender', 'danwei', 'dishi']
    # 关闭书签功能
    show_bookmarks = False
    # 设置载入自定义按钮，创建下载模板
    meeting_allow = True
    # 排序使用
    ordering = ['id']
    # 输入框只读设置
    # readonly_fields = ['user']
    # 不在输入框显示设置
    exclude = ['user']

    def __unicode__(self):
        return self.name

    def save_models(self):
        self.new_obj.user = self.request.user
        self.new_obj.save()

    # #设计只能查看自己的创建的内容
    def queryset(self):
        if not self.request.user.is_superuser:
            st = self.request.user
            sr = Meeting.objects.filter(user=st)
            return sr
        return Meeting.objects.all()


    #=================进行设置添加表单时的样式设置====================================
    form_layout = (
        Main(
            Fieldset('',
                     'name', 'gender',
                     css_class='unsort no_title'
                     ),
            Fieldset('Personal info',
                     Row('danwei', 'dishi'),
                     'mobile'
                     ),
        ),
        # Side(
        #     Fieldset(_('Status'),
        #              'is_active', 'is_staff', 'is_superuser',
        #              ),
        # )
    )


# ==============下面自己引入的按钮插件======================
class MeetingPlugin(BaseAdminPlugin):
    meeting_allow = False

    def init_request(self, *args, **kwargs):
        return bool(self.meeting_allow)

    def block_top_toolbar(self, context, nodes):
        context.update({
            'options': ['install', 'unstall']
        })

        nodes.append(loader.render_to_string(
            'model_list.top_toolbar.sdp.html',
            context=get_context_dict(context)
        ))


xadmin.site.register_plugin(MeetingPlugin, ListAdminView)
