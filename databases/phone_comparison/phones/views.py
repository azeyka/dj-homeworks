from django.shortcuts import render
from .models import Phone, Samsung, Apple


def show_catalog(request):
    def add_characteristic_names():
        for model in [Phone, Samsung, Apple]:
            for name in model._meta.get_fields():
                if hasattr(name, 'verbose_name'):
                    if name.name != 'info' and name.name != 'id':
                        characteristics[name.name] = [name.verbose_name.capitalize()]


    def add_characteristic_values():
        for model in [Samsung, Apple]:
            for phone in model.objects.all().select_related():
                for name in characteristics.keys():
                    try:
                        val = phone.__getattribute__(name)
                    except:
                        try:
                            val = phone.info.__getattribute__(name)
                        except:
                            val = '-'

                    if val == True:
                        val = '+'
                    elif val == False:
                        val = '-'

                    characteristics[name].append(val)

    characteristics = {}
    add_characteristic_names()
    add_characteristic_values()

    return render(
        request,
        'catalog.html',
        context={
            'characteristics': characteristics
        }
    )
