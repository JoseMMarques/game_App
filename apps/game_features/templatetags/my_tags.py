from django import template

register = template.Library()


@register.filter()
def get_field_name(object, field):
    verbose_name = object.get_field(field).verbose_name
    return verbose_name


@register.filter
def verbose_name_plural(obj):
    return obj._meta.verbose_name_plural


# não ir por aqui
#disable all form
#ver ---
#https://stackoverflow.com/questions/55506000/syntax-for-disabling-all-form-fields-in-django
