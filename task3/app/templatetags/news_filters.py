from django import template
import datetime
import time


register = template.Library()


@register.filter
def format_date(value):

    delta = time.time() - value

    if delta < 600:
        return 'ТОЛЬКО ЧТО'
    elif 600 <= delta < 86400:
        result = int(delta / 3600)
        return f'{result} часов назад'
    else:
        return datetime.datetime.fromtimestamp(delta).strftime('%Y-%M-%d')

@register.filter
def format_num_comments(value):

    if 0 < value <= 50:
        return f'<b>{value}</b>'

    elif value > 50:
        return '<b>50+</b>'

    elif value == 0:
        return '<u>Оставьте комментарий</u>'


@register.filter
def score_format(value: int, arg: str):
    if value < -5:
        return 'всё плохо'
    elif -5 < value < 5:
        return 'нейтрально'
    elif 5 < value:
        return 'хорошо'
    elif value == None:
        return arg


@register.filter
def format_selftext(value: str, count) -> str:
    text_split = value.split()
    count = int(count)

    if len(text_split) <= count*2:
        return f'TOO SHORT {value}'

    left = ' '.join(text_split[:count])
    right = ' '.join(text_split[-count:])

    return f'{left}  . . .  {right}'
