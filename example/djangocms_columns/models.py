import threading

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable
from tinymce import models as tinymce_models
from filebrowser.fields import FileBrowseField

import utils

localdata = threading.local()
localdata.TEMPLATE_CHOICES = utils.autodiscover_templates()
TEMPLATE_CHOICES = localdata.TEMPLATE_CHOICES


class ColumnsPlugin(CMSPlugin):

    def copy_relations(self, oldinstance):
        for col in oldinstance.column_set.all():
            new_col = Column()
            new_col.columns = self
            new_col.src = col.src
            new_col.src_height = col.src_height
            new_col.src_width = col.src_width
            new_col.title = col.title
            new_col.alt = col.alt
            new_col.save()

    template = models.CharField(max_length=255,
                                choices=TEMPLATE_CHOICES,
                                default='djangocms_columns/columns.html',
                                editable=len(TEMPLATE_CHOICES) > 1)

    def __unicode__(self):
        return _(u'%(count)d col(s) in columns') % {'count': self.column_set.count()}


class Column(Orderable):

    def get_media_path(self, filename):
        pages = self.columns.placeholder.page_set.all()
        return pages[0].get_media_path(filename)

    columns = models.ForeignKey(ColumnsPlugin, verbose_name=_("Columns"))
    src = FileBrowseField("Column", max_length=200, directory="/", blank=True)
    src_height = models.PositiveSmallIntegerField(_("Column height"), editable=False, blank=True)
    src_width = models.PositiveSmallIntegerField(_("Column height"), editable=False, blank=True)
    title = models.CharField(_("Title"), max_length=255, blank=True)
    alt = tinymce_models.HTMLField()

    def __unicode__(self):
        return self.title or self.alt or str(self.pk)
