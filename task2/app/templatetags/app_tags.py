from django import template


register = template.Library()


@register.filter
def is_active(value, arg):
	if value == arg:
		return 'active'
