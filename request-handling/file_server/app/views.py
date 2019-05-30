import datetime
import os

from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'
    context = {
        'files': [],
    }

    files = os.listdir(settings.FILES_PATH)

    for file_name in files:
        file_path = os.path.join(settings.FILES_PATH, file_name)
        file_info = os.stat(file_path)

        ctime = datetime.datetime.fromtimestamp(int(file_info.st_ctime))
        mtime = datetime.datetime.fromtimestamp(int(file_info.st_mtime))

        info = {
            'name': file_name,
            'ctime': convert_date(ctime),
            'mtime': convert_date(mtime)
                }

        if date:
            [year, month, day] = date.split('-')

            if int(year) == ctime.year and int(month) == ctime.month and int(day) == ctime.day:
                context['files'].append(info)
                context['date'] = f'{day} {convert_month(int(month))} {year} г.'
        else:
            context['files'].append(info)

    return render(request, template_name, context)

def file_content(request, name):
    file_path = os.path.join(settings.FILES_PATH, name)
    with open(file_path, 'r') as file:
        text = file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': text}
    )

def convert_date(date):
    return {
        'date': f'{date.year}-{date.month}-{date.day}',
        'date_to_show': f'{date.day} {convert_month(date.month)} {date.year} г.',
        'time': f'{date.hour}:{date.minute}'
    }

def convert_month(month_num):
    if month_num == 1:
        return 'января'
    elif month_num == 2:
        return 'февраля'
    elif month_num == 3:
        return 'марта'
    elif month_num == 4:
        return 'апреля'
    elif month_num == 5:
        return 'мая'
    elif month_num == 6:
        return 'июня'
    elif month_num == 7:
        return 'июля'
    elif month_num == 8:
        return 'августа'
    elif month_num == 9:
        return 'сентября'
    elif month_num == 10:
        return 'октября'
    elif month_num == 11:
        return 'ноября'
    elif month_num == 12:
        return 'декабря'
