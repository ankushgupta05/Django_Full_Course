from django.shortcuts import render
from django.http import HttpResponse

# import Product 
from .models import Product,Contact

# import ceil function 
from math import ceil



# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = { item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1,nSlides),nSlides])
    param = {'allProds':allProds}
    # print(allProds)
    return render(request,'shop/index.html',param)


def about(request):
    return render(request,'shop/about.html')
    # return HttpResponse("This is  a page of  about")


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        # print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')
    # return HttpResponse("This is  a page of contact")


def tracker(request):
    return render(request,'shop/tracker.html')
    # return HttpResponse("This is  a page of tracker")


def search(request):
    return render(request,'shop/search.html')
    # return HttpResponse("This is  a page of search")


def productView(request,myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/prodView.html',{'product':product[0]})
    # return HttpResponse("This is  a page of Product view")


def checkout(request):
    return render(request,'shop/checkout.html')
    # return HttpResponse("This is  a page of checkout")





#  Here Experiment index_backup_experiment.html

def index_backup(request):
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = { item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1,nSlides),nSlides])
    param = {'allProds':allProds}
    # print(allProds)
    return render(request,'shop/index_2_backup_experiment.html',param)

