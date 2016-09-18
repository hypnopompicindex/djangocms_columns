from inline_ordering.admin import OrderableStackedInline
import forms
import models


class ColumnInline(OrderableStackedInline):

    model = models.Column

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'src':
            kwargs.pop('request', None)
            kwargs['widget'] = forms.AdminColumnWidget
            return db_field.formfield(**kwargs)
        return super(ImageInline, self).\
            formfield_for_dbfield(db_field, **kwargs)
