from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
from .models import Product, Category
from cart.forms import CartAddProductForm


def product_list(request, category_slug = None):
    
    if request.path == '/':
        products = Product.objects.filter(
            available = True,
            is_popular = True
        ).order_by('name')

        context = {
            'products':products,
            'category':category_slug,        
        }

        return render(request, 'shop/product/product_list.html', context=context)


    query = request.GET.get('q')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

        products = Product.objects.filter(
                category = category,
                available = True,
            ).order_by('name')

    
        if query:
            products = products.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query) )

        context = {
            'products':products,
            'category':category_slug,
            'query':query
        }

        return render(request, 'shop/product/product_list.html', context=context)

    # ===== 3️⃣ КАТАЛОГ =====
    products = Product.objects.filter(available=True)
    query = request.GET.get('q', '').strip()
    sort = request.GET.get('sort')

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query))

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')
    else:
        products = products.order_by('name')

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'shop/product/catalog.html', {
        'products': products, 'query': query, 'current_sort': sort,})



def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    # return render(request, 'shop/product/detail.html', {'product': product})
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})