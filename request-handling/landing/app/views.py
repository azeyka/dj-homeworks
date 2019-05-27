from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    arg = request.GET.get('from-landing')
    counter_click[arg] += 1
    return render_to_response('index.html')


def landing(request):
    arg = request.GET.get('ab-test-arg')
    counter_show[arg] += 1

    if arg == 'original':
        return render_to_response('landing.html')
    elif arg == 'test':
        return render_to_response('landing_alternate.html   ')


def stats(request):
    landing_stats = {
        'original' : 0,
        'test' : 0
    }

    for landing in landing_stats.keys():
      if counter_show[landing] != 0:
         landing_stats[landing] = counter_click[landing] / counter_show[landing]

    return render_to_response('stats.html', context={
        'test_conversion': landing_stats['test'],
        'original_conversion': landing_stats['original'],
    })
