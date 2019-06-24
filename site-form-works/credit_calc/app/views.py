from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"
    form = CalcForm()
    context = {}

    def get(self, request, *args, **kwargs):
        form = CalcForm(self.request.GET)
        if form.is_valid():
            inital_fee = form.cleaned_data['initial_fee']
            rate = form.cleaned_data['rate']
            months_count = form.cleaned_data['months_count']
            common_result = round((inital_fee + inital_fee * rate) / months_count)
            result = round(common_result / months_count)
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'result': result,
                    'common_result': common_result
                }
            )

        return render(request, self.template_name, {'form': form})
