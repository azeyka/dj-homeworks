from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm
from django.shortcuts import render

class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    model = Product
    template_name = "app/product_detail.html"

    def get_object(self, queryset=None):
        return Product.objects.get(id=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')

        reviews = Review.objects.all().filter(product_id=id)
        context['reviews'] = reviews

        reviewed_products = self.request.session.get('reviewed_products')
        if reviewed_products and id in reviewed_products:
            context['is_review_exist'] = True
        else:
            context['form'] = ReviewForm

        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        form = ReviewForm(self.request.POST)

        if form.is_valid():
            Review.objects.create(text=form.cleaned_data['text'], product_id=pk)

            if not self.request.session.get('reviewed_products'):
                self.request.session['reviewed_products'] = []

            self.request.session['reviewed_products'].append(pk)
            self.request.session.modified = True

        return redirect('product_detail', pk=pk)