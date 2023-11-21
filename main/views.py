from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.contrib import messages
from django.core import serializers
from django.shortcuts import render
from main.forms import ProductForm
from main.models import Product
from functools import reduce
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt
@login_required(login_url='main:login')
def increment(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        product.amount += 1
        product.save()
    return redirect('main:index')


@csrf_exempt
@login_required(login_url='main:login')
def decrement(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        product.amount -= 1
        product.save()
    return redirect('main:index')


@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Product(name=name, price=price,
                              amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(new_product.pk, status=201)

    return HttpResponseNotFound()


@csrf_exempt
@login_required(login_url='main:login')
def delete(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        product.delete()
    return redirect('main:index')


@login_required(login_url='main:login')
def index(request):
    products = Product.objects.all()
    stocks = reduce(lambda x, y: x + y,
                    [product.amount for product in products])
    context = {
        'products': products,
        'stocks': stocks,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, 'index.html', context=context)


@csrf_exempt
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid() and request.method == 'POST':
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:index')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='main:login')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect("main:index")
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


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_product = Product.objects.create(
            user=request.user,
            name=data["name"],
            amount=int(data["amount"]),
            price=int(data["price"]),
            description=data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
