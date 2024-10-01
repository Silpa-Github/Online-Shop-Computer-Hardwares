from django.shortcuts import render,redirect
import datetime
from SparrowApp.models import CategoryDb,Productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from frontendApp.models import ContactDB,LoginDB
# Create your views here.
def home(request):
    today=datetime.datetime.now()
    return render(request,'index.html',{'today':today})
def add_category(request):
    return render(request,'add_category.html')
def add_product(request):
    category=CategoryDb.objects.all()
    return render(request,'add_product.html',{'category':category})
def category_details(request):
    data=CategoryDb.objects.all()
    return render(request,'category_details.html',{'data':data})
def product_details(request):
    data=Productdb.objects.all()
    return render(request,'view_product.html',{'data':data})

def save_category(request):
    if request.method == "POST":
        item=request.POST.get('item')
        image=request.FILES['image']
        description=request.POST.get('description')
        obj=CategoryDb(item=item,image=image,description=description)
        obj.save()
        return redirect(add_category)
def save_product(request):
    if request.method == "POST":
        category=request.POST.get('category')
        product_name = request.POST.get('product_name')
        company = request.POST.get('company')
        price = request.POST.get('price')
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        image3=request.FILES['image3']
        specification=request.POST.get('spec')
        description = request.POST.get('desc')
        obj=Productdb(category=category,product_name=product_name,company=company,price=price,image1=image1,image2=image2,image3=image3,description=description,specification=specification)
        obj.save()
        return redirect(add_product)
def edit_category(request,category_id):
    data=CategoryDb.objects.get(id=category_id)
    return render(request,'edit_category.html',{'data':data})
def edit_product(request,pro_id):
    cat=CategoryDb.objects.all()
    data=Productdb.objects.get(id=pro_id)
    return render(request,'edit_product.html',{'data':data,'cat':cat})
def update_category(request,category_id):
    if request.method == "POST":
        item=request.POST.get('item')
        description = request.POST.get('description')
        try:
            image=request.FILES['image']
            fs= FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=category_id).image
        CategoryDb.objects.filter(id=category_id).update(item=item,image=file,description=description)
        return redirect(category_details)
def update_product(request,pro_id):
    if request.method == "POST":
        category = request.POST.get('category')
        product_name = request.POST.get('product_name')
        company = request.POST.get('company')
        price = request.POST.get('price')
        try:
            image=request.FILES['image1']
            fs= FileSystemStorage()
            file1=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file1=Productdb.objects.get(id=pro_id).image1
        try:
            image=request.FILES['image2']
            fs= FileSystemStorage()
            file2=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file2=Productdb.objects.get(id=pro_id).image2
        try:
            image=request.FILES['image3']
            fs= FileSystemStorage()
            file3=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file3=Productdb.objects.get(id=pro_id).image3
        specification = request.POST.get('spec')
        description = request.POST.get('desc')

        Productdb.objects.filter(id=pro_id).update(category=category,product_name=product_name,company=company,price=price,image1=file1,image2=file2,image3=file3,specification=specification,description=description)
        return redirect(product_details)
def delete_category(request,category_id):
    x=CategoryDb.objects.filter(id=category_id)
    x.delete()
    return redirect(category_details)
def delete_product(request,pro_id):
    x=Productdb.objects.filter(id=pro_id)
    x.delete()
    return redirect(product_details)
def admin_loginpage(request):
    return render(request,'adminlogin.html')
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(home)
            else:
                return redirect(admin_loginpage)
        else:
            return redirect(admin_loginpage)
    return redirect(admin_loginpage)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)
def contactdetails(request):
    msg=ContactDB.objects.all()
    return render(request,'contactdetails.html',{'msg':msg})
def deletecontactmessage(request,contact_id):
    x=ContactDB.objects.filter(id=contact_id)
    x.delete()
    return redirect(contactdetails)
def user_login_data(request):
    data=LoginDB.objects.all()
    return render(request,'user_login_data.html',{'data':data})
def delete_user(request,user_id):
    x=LoginDB.objects.filter(id=user_id)
    x.delete()
    return redirect(user_login_data)