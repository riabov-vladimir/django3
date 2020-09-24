from django import template
import datetime
import time


register = template.Library()


@register.filter
def format_date(value):

    delta = time.time() - value
    print(delta)
    if delta < 600:
        return 'ТОЛЬКО ЧТО'
    elif 600 <= delta < 86400:
        result = int(delta / 3600)
        return f'{result} часов назад'
    else:
        return datetime.datetime.fromtimestamp(delta).strftime('%Y-%M-%d')


"""format_date: форматирует дату по следующим правилам
Если пост был меньше 10 минут назад, пишет "только что"
Если пост был меньше 24 часов назад, пишет "X часов назад"
Если пост был больше 24 часов назад, выводит дату в формате "Год-месяц-число"""

# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):

    if 0 < value <= 50:
        return f'<b>{value}</b>'

    elif value > 50:
        return '<b>50+</b>'

    elif value == 0:
        return '<u>Оставьте комментарий</u>'

"""
Приложение выводит самые лучшие свежие посты из сабреддита, посвященному Python (reddit.com/r/Python).

В директории templatetags/news_filters.py необходимо реализовать следующие фильтры:


форматирование поля score (название на ваше усмотрение):
Рейтинг меньше -5, пишет "все плохо"
Рейтинг от -5 до 5 – "нейтрально"
Рейтинг больше 5 – "хорошо"
Если поле score отсутствует, то рендерится дефолтное значение, которое передается в качестве параметра фильтра.

format_num_comments:
Если комментариев 0, пишется "Оставьте комментарий"
От 0 до 50, пишем число комментариев
Больше 50, пишем "50+"
format_selftext:
Оставляет count первых и count последних слов, между ними должно быть троеточие. count задается параметром фильтра. Пример c count = 5: "Hi all sorry if this ... help or advice greatly appreciated."

Знаки препинания остаются, обрезаются только слова.
"""

if __name__ == '__main__':

    value = 100893867

    print(format_date(value))
