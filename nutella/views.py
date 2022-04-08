"""Module providing views to app nutella"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from off.models import Favorite, Product


# Create your views here.
def index(request):
    """generic view"""
    return render(request,'nutella/index.html')

def product(request, pk):
    """detail product view"""
    detail = Product.objects.get(pk=pk)
    context = {"product":detail}
    return render(request,'nutella/product.html', context)

def search_product(request):
    """search view for index search"""
    search_term = request.GET.get('home_search')
    context = {
        'product_list':Product.objects.filter(product__search=search_term).order_by('product'),
        'search_term': search_term
    }
    return render(request, 'nutella/product_search.html', context)

def search_replacement(request, pk):
    """search view for product replacement"""
    context={
        'result_list':None,
        'product_name':None,
        'product_score':None,
        'product_image': None,
        'product_id':0
    }

    base_product = Product.objects.select_related('category_id').get(pk=pk)
    context['product_name']=base_product.product
    context['product_score']=base_product.score
    context['product_image']= base_product.pic_url
    context['product_id']= base_product.id

    global_queryset = (Product.objects.select_related('category_id')
                       .filter(category_id__exact=base_product.category_id)
                       .exclude(pk=base_product.pk))

    context['result_list'] = global_queryset.filter(score__lt=base_product.score).order_by('score', 'product')

    return render(request, 'nutella/product_replacement.html', context)

@login_required
def save_favorite(request, pk_replaced, pk_replacing):
    """save replacement product in database for the current user"""
    replaced = Product.objects.get(id=pk_replaced)
    replacing = Product.objects.get(id=pk_replacing)
    
    Favorite.objects.create(
        product_id = replaced,
        replacement_id = replacing,
        user_id = request.user)
    
    previous_url = request.META.get('HTTP_REFERER')
    return redirect(previous_url)

@login_required
def delete_favorite(request, pk):
    """delete replacement product in database for the current user"""
    Favorite.objects.filter(id__exact=pk).delete()
    previous_url = request.META.get('HTTP_REFERER')
    return redirect(previous_url)

@login_required
def product_user(request, pk):
    """display favorite recorded product for current user"""
    queryset = Favorite.objects.filter(user_id__exact=pk)
    context={'product_list': queryset }
    return render(request, 'nutella/product_user.html', context)

def legal_notice(request):
    """display legal notice"""
    return render(request, 'nutella/legal_notice.html')
