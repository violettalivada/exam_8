from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product
from webapp.forms import ProductForm


class IndexView(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        return Product.objects.all().order_by('name')


class ProductView(DetailView):
    template_name = 'product/product.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        reviews = product.reviews.order_by('author')
        context['reviews'] = reviews
        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'product/update.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'product/delete.html'
    model = Product
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_product')