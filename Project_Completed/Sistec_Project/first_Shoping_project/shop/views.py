from django.shortcuts import render
from django.http import HttpResponse
import json

# import for payment securety
from django.views.decorators.csrf import csrf_exempt

# import Product Contact Order
from .models import Product,Contact,Order,OrderUpdate


# import ceil function 
from math import ceil

#  import logging library
import logging
logger = logging.getLogger(__name__)



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
    params = {'allProds':allProds}
    # print(allProds)
    return render(request,'shop/index.html',params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False
    # return True
def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = { item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [ item for item in prodtemp if searchMatch(query , item) ]
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        if len(prod) != 0:
            allProds.append([prod, range(1,nSlides),nSlides])
    params = {'allProds':allProds,"msg":""}
    # print(len(allProds))
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg':"Please Make sure to enter relevant search query"}
    
    return render(request,'shop/search.html',params)

    
    
    # return render(request,'shop/index.html')
    # # return HttpResponse("This is  a page of search")


def about(request):
    return render(request,'shop/about.html')
    # return HttpResponse("This is  a page of  about")


def contact(request):
    thank = False
    if request.method == "POST":
        # print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        # print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank = True
    return render(request,'shop/contact.html',{'thank':thank})
    # return HttpResponse("This is  a page of contact")


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates =[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps({"status":"success","updates":updates,"itemsJson":order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
        
    return render(request,'shop/tracker.html')
    # return HttpResponse("This is  a page of tracker")





def productView(request,myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/prodView.html',{'product':product[0]})
    # return HttpResponse("This is  a page of Product view")


def checkout(request):
    if request.method == "POST":
        # print(request)
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        amount = request.POST.get('amount','')
        email = request.POST.get('email','')
        address = request.POST.get('address','') + " " + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        # desc = request.POST.get('desc','')
        order = Order(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        # return render(request,'shop/checkout.html',{'thank':thank,'id':id})
        # request paytm to transfer the amount after paytm by user
        # Request paytm to transfer the amount to your account after payment by user
        
        
    return render(request,'shop/checkout.html')
    # return HttpResponse("This is  a page of checkout")

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    pass
    
    



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

