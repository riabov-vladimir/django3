from django.template import library


register = library.Library()


@register.filter
def table_color(value):
	"""
	Если инфляция за месяц была отрицательной (дефляция), то ячейка должна быть закрашена
	в зеленый. Если значение инфляции превысило 1%, то в красный. Должна быть
	реализована визуальная градация красного: от 1% до 2%, от 2% до 5%,
	от 5% и более (3 оттенка красного, визуально они должны быть различимы).
	:param value:
	:return:
	"""
	try:
		value = float(value)
	except ValueError:
		return 'white'

	if value < 0:
		return '#32a852'
	elif 1 < value < 2:
		return '#ff6969'
	elif 2 < value < 5:
		return '#ff4242'
	elif 5 < value:
		return '#ff0000'
	else:
		return 'white'


@register.filter
def is_data(value):
	if not value:
		return '-'
	else:
		return value
