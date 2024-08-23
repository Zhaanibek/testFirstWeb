from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from goods.models import ProductCarRental, ProductSpare


def catalogCarRental(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'default')

    if category_slug == 'vse-kategorii':
        goods = ProductCarRental.objects.all()
    else:
        goods = ProductCarRental.objects.filter(category__slug=category_slug)

    if order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.get_page(page)

    context = {
        'title': 'Home - Catalog Rentals',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def catalogSpare(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'default')

    if category_slug == 'vse-kategorii':
        goods = ProductSpare.objects.all()
    else:
        goods = ProductSpare.objects.filter(category__slug=category_slug)

    if order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.get_page(page)

    context = {
        'title': 'Home - Catalog Spares',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug=None, product_id=None):
    if product_id:
        product = ProductCarRental.objects.filter(id=product_id).first() or ProductSpare.objects.filter(id=product_id).first()
    else:
        product = ProductCarRental.objects.filter(slug=product_slug).first() or ProductSpare.objects.filter(slug=product_slug).first()

    if not product:
        raise Http404("Product not found")

    context = {
        'product': product
    }
    return render(request, 'goods/products.html', context)
