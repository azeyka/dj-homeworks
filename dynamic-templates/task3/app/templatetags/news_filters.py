from django import template
import datetime


register = template.Library()


@register.filter
def format_date(value):
    now = datetime.datetime.now()
    post_time = datetime.datetime.fromtimestamp(value)

    delta = now - post_time
    minutes = delta.total_seconds() / 60
    hours = delta.total_seconds() / 3600

    if minutes <= 10:
        return 'Только что'
    else:
        if hours < 24:
            return f'{round(hours)} часов назад'
        else:
            return f'{post_time.year}-{post_time.month}-{post_time.day}'

@register.filter
def format_rating(value, default_value=0):
    if not value:
        value = default_value

    if value < -5:
        return 'все плохо'
    elif 5 > value > -5:
        return 'нейтрально'
    elif value > 5:
        return 'хорошо'

@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif value > 50:
        return '50+'

    return value

@register.filter
def limit_text(text, count):
    if text:
        splitted = text.split(' ')
        begin = splitted[:count]
        end = splitted[-count:]
        return f"{' '.join(begin)} ... {' '.join(end)}"

    return ''