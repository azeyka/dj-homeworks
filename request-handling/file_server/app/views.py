import datetime
import os

from django.shortcuts import render
    from django.conf import settings

def file_list(request, year=None, month=None, day=None):
    template_name = 'index.html'
    context = {
        'files': []
        # 'date': datetime.date(2018, 5, 1)  # Этот параметр необязательный
    }

    files = os.listdir(settings.FILES_PATH)

    for file_name in files:
        file_path = os.path.join(settings.FILES_PATH, file_name)
        file_info = os.stat(file_path)

        ctime = datetime.datetime.fromtimestamp(int(file_info.st_ctime))
        mtime = datetime.datetime.fromtimestamp(int(file_info.st_mtime))

        info = {
            'name': file_name,
            'ctime': str(ctime),
            'mtime': str(mtime)
                }

        if year and month and day:
            print(year, month, day)
            if year == ctime.year and month == ctime.month and day == ctime.day:
                context['files'].append(info)
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

