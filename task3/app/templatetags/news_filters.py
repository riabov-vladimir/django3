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
def score_format(value):
    if value < -5:
        return 'всё плохо'
    elif -5 < value < 5:
        return 'нейтрально'
    elif 5 < value:
        return 'хорошо'



"""

форматирование поля score (название на ваше усмотрение):
Рейтинг меньше -5, пишет "все плохо"
Рейтинг от -5 до 5 – "нейтрально"
Рейтинг больше 5 – "хорошо"
Если поле score отсутствует, то рендерится дефолтное значение, которое передается в качестве параметра фильтра.

format_selftext:
Оставляет count первых и count последних слов, между ними должно быть троеточие.
 count задается параметром фильтра. Пример c count = 5: "Hi all sorry if this ... help or advice greatly appreciated."

Знаки препинания остаются, обрезаются только слова.
"""

if __name__ == '__main__':

    pass