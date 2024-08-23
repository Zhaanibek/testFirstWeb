from django.shortcuts import render
from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from blog.models import Post

def catalogBlog(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'vse-kategorii':
        goods = Post.objects.all()
        
    else:
        goods = Post.objects.filter(category__slug=category_slug)


    if order_by and order_by != 'default':
        goods = sorted(goods, key=lambda x: getattr(x, order_by))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - catalog',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'blog/catalog.html', context)


def product(request, product_slug=False, product_id=False):
    if product_id:
        product = Post.objects.filter(id=product_id).first()
    else:
        product = Post.objects.filter(slug=product_slug).first()
    if not product:
        raise get_list_or_404("Product not found")

    context = {
        'product': product
    }
    return render(request, 'blog/products.html', context)