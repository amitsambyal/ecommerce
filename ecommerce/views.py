from django.shortcuts import render
from ecom.models import Category,Subcategory,Product


#def master(request):
 #   return render(request,'master.html')

def index(request):
    
    category=Category.objects.all()
    
    categoryid=request.GET.get('category')
    
    if categoryid:
        product=Product.objects.filter(sub_category=categoryid)
    else:
        product=Product.objects.all()    
        
    context={
        'category':category,
        'product':product,
    }
    
    return render(request,'index.html',context)

def login_page(request):
    return render(request, 'login.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def product_details(request):
    return render(request, 'product-details.html')

def shop(request):
    return render(request, 'shop.html')


