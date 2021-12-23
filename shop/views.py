
from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def Home(request,cat_slug=None):
    cat_page = None
    product = None

    if cat_slug is not None:
        cat_page = get_object_or_404(Category,slug=cat_slug)
        product = Product.objects.filter(prodcat=cat_page,avail=True)
    else:
        product = Product.objects.all().filter(avail=True)
    cat_home = Category.objects.all()     
    paginator = Paginator(product,4)

    try:
        page = int(request.GET.get('page_num','1'))
    except:
        page = 1
    try:
        pages = paginator.page(page)
    except(EmptyPage,InvalidPage):
        pages = paginator.page(paginator.num_pages)
    return render(request, 'Index.html', {'prd':product, 'cat_home':cat_home, 'page_num':pages})

def product_Details(request,cat_slug,prd_slug):
    try:
        prod = Product.objects.get(prodcat__slug=cat_slug,slug=prd_slug)
    except Exception as e:
        raise e
    return render(request,'Item.html', {'prd':prod})

def search(request):
    sr_prod = None
    sr_query = None

    if 'q' in request.GET:
        sr_query = request.GET.get('q')
        sr_prod = Product.objects.all().filter(Q(name__contains=sr_query) | Q(desc__contains=sr_query))
    return render(request,'Search.html',{'qry':sr_query,'prdct':sr_prod})