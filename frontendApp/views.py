from django.shortcuts import render,redirect
from frontendApp.models import ContactDB,LoginDB,CartDB,CheckoutDB
from SparrowApp.models import CategoryDb,Productdb
from django.contrib import messages
import razorpay

# Create your views here.
def webindex(request):
    category=CategoryDb.objects.all()
    product=Productdb.objects.all()
    return render(request,'webindex.html',{'category':category,'product':product})
def aboutus(request):
    return render(request,'Aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
def save_contact_message(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        Email_id=request.POST.get('Email_id')
        Message=request.POST.get('Message')
        obj=ContactDB(Name=Name,Email_id=Email_id,Message=Message)
        obj.save()
        return redirect(contactus)
def productlist(request):
    prod=Productdb.objects.all()
    cat=CategoryDb.objects.all()
    return render(request,'productlist.html',{'cat':cat,'prod':prod})
def single_product(request,pro_id):
    prod = Productdb.objects.get(id=pro_id)
    products = Productdb.objects.all()
    cat = CategoryDb.objects.all()
    return render(request,'single_product.html',{'cat':cat,'prod':prod,'products':products})
def filtered_products(request,cat_name):
    cat = CategoryDb.objects.all()
    data=Productdb.objects.filter(category=cat_name)
    return render(request,'filtered_products.html',{'cat':cat,'data':data})
def login_page(request):
    return render(request,'login_page.html')
def save_user_signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email_id=request.POST.get('email_id')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        obj=LoginDB(username=username,email_id=email_id,password1=password1,password2=password2)
        obj.save()
        messages.success(request, 'Registered Successfully.Now you can login!')
        return redirect(login_page)
def user_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if LoginDB.objects.filter(username=un,password1=pwd).exists():
            request.session['username']=un
            request.session['password1']=pwd
            messages.success(request,'login successfully')
            return redirect(webindex)
        else:
            messages.warning(request,'User not found')
            return redirect(login_page)
    else:
        messages.warning(request, 'Invalid credentials')
        return redirect(login_page)
def logout_user(request):
    del request.session['username']
    del request.session['password1']
    return redirect(webindex)
def addtocart(request):
    if request.method=="POST":
        username=request.POST.get("username")
        productname = request.POST.get("productname")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        total = request.POST.get("total")
        obj=CartDB(Username=username,Productname=productname,Quantity=quantity,Price=price,Totalprice=total)
        obj.save()
        messages.success(request,'item added to cart')
        return redirect(webindex)
def cartpage(request):
    data=CartDB.objects.filter(Username=request.session['username'])
    category=CategoryDb.objects.all()
    subtotal=0
    shipping=0
    total=0
    for i in data:
        subtotal+=i.Price
        if subtotal>3000:
            shipping=150
        else:
            shipping=250
    total=shipping+subtotal

    return render(request,'cart.html',{'data':data,'category':category,'subtotal':subtotal,'total':total,'shipping':shipping})

def deletecartitem(request,dataid):
    x=CartDB.objects.filter(id=dataid)
    x.delete()
    messages.success(request,'item deleted from cart')
    return redirect(cartpage,)
def checkout(request):
    data=CartDB.objects.filter(Username=request.session['username'])
    subtotal = 0
    shipping = 0
    total = 0
    for i in data:
        subtotal += i.Price
        if subtotal > 3000:
            shipping = 150
        else:
            shipping = 250
    total = shipping + subtotal
    return render(request,'checkout.html',{'data':data,'subtotal':subtotal,'shipping':shipping,'total':total})
def save_checkout_data(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        city = request.POST.get('city')
        total=request.POST.get('total')
        obj=CheckoutDB(name=name,email=email,mobile=mobile,address=address,city=city,total=total)
        obj.save()
        return redirect(payment)
def payment(request):
    customer = CheckoutDB.objects.order_by('-id').first()
    payy = customer.total
    amount = int(payy * 100)
    payy_str = str(amount)

    for i in payy_str:
        print(i)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_Iqp5fIab1M5Oe2', 'Mm9YS7DOCvvnRASizO8QmsTJ'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})
    return render(request, "payment.html", {'customer': customer, 'payy_str': payy_str})
