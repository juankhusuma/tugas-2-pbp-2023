from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from main.forms import ProductForm
from main.models import Product
from functools import reduce

# Create your views here.


def index(request):
    products = Product.objects.all()
    stocks = reduce(lambda x, y: x + y,
                    [product.amount for product in products])
    return render(request, 'index.html', {'products': products, 'stocks': stocks})


def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return index(request)
    context = {'form': form}
    return render(request, 'add_product.html', context)


def show_products_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return HttpResponse(data, content_type='application/json')


def show_product_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')


def show_product_json_by_id(request, id):
    product = Product.objects.get(pk=id)
    data = serializers.serialize('json', [product])
    return HttpResponse(data, content_type='application/json')


def show_product_xml_by_id(request, id):
    product = Product.objects.get(pk=id)
    data = serializers.serialize('xml', [product])
    return HttpResponse(data, content_type='application/xml')
