from django.shortcuts import render
from .models import *
from .forms import ContactFrom
from django.db.models import Q

# Create your views here.


def index(request):
    banner = Banner.objects.all()
    catagorys = Catagory.objects.all()
    brand = Brand.objects.all()
    product = Prodact.objects.all()
    fasion = Prodact.objects.filter(catagory__name ='Fashion')
    food = Prodact.objects.filter(catagory__name ='Food')

    context = {
        'banner':banner,
        'catagorys':catagorys,
        'brand':brand,
        'product':product,
        'fasion':fasion,
        'food':food
    }

    return render(request, 'myapp/index.html', context)

def product_details(request, pk):
    product = Prodact.objects.get(pk=pk)
    releted_product = Prodact.objects.filter(Q(catagory=product.catagory) | Q(brand=product.brand)).exclude(pk=pk)
    
    context ={
        'product':product,
        'releted_product':releted_product
    }
    return render(request, 'myapp/product.html', context)

def product_search(request):
    query = request.GET['q']
    lookup =Q(name__icontains=query) | Q(catagory__name__icontains=query) | Q(brand__name__icontains=query)
    products = Prodact.objects.filter(lookup)

    context ={
        'products':products
        
    }
    return render(request,'myapp/product-search.html',context)

def contact (request):

    form = ContactFrom(request.POST)
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#home')
    context = {
        'form':form
    }
    return render(request, 'myapp/contact.html',context)

def aboutus (request):
    about  = About.objects.last()
    return render(request, 'myapp/about.html',{'about':about})