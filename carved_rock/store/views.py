from django.shortcuts import render

from carved_rock.store.models import Product


def category_view(request, name):
    products = Product.Objects.filter(category_name=name)

    return render(request, "store/category.html",
                  {'products': products,
                           'category_name': name})
