import datetime
import os

from django.shortcuts import render
from django.conf import settings
from django.http import Http404


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
            'ctime': ctime,
            'mtime': mtime
                }

        if date:
            try:
                f_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                if f_date.date() == ctime.date():
                    context['files'].append(info)
            except:
                raise Http404
        else:
            context['files'].append(info)

    if date:
        context['date'] = f_date.date()

    return render(request, template_name, context)

def file_content(request, name):
    file_path = os.path.join(settings.FILES_PATH, name)

    if not os.path.isfile(file_path):
        raise Http404

    with open(file_path, 'r') as file:
        text = file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': text}
    )