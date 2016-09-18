from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

import admin
import models


class CMSColumnsPlugin(CMSPluginBase):

    model = models.ColumnsPlugin
    inlines = [admin.ColumnInline, ]
    name = _('Columns')
    render_template = 'djangocms_columns/columns.html'

    def render(self, context, instance, placeholder):
        context.update({
                        'column': instance.column_set.all(),
                        'columns': instance,
                       })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSColumnsPlugin)
