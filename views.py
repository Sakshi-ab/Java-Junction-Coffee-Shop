from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from javajunctionapp.models import product,Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Order, product
from .form import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def create(request):
   # print(request.method)
   if request.method == 'GET':
    return render(request,'create.html')
   elif request.method == 'POST':
     #else me post method hai and wo data send krra hai sql me
     name = request.POST['name']
     
     price = request.POST['price']
     
     details = request.POST['detail']
     
     category = request.POST['category']

     image = request.FILES['upload']

     

     M = product.objects.create(name = name, price = price, details = details, category = category, image = image)  # create method query create krega
     M.save()  #actually save method execute krega

     v = product.objects.all()
     context = {}
     context['data'] = v
     return render(request,"dashboard.html", context )
     

def dashboard(request):
       
       m = product.objects.all()
       context = {}

       context['data'] = m
       
       return render(request,'dashboard.html', context)

       


def delete(request,rid):
   m = product.objects.filter(id = rid)
   m.delete()
   return redirect('/dashboard')

def edit(request, rid):
   if request.method == 'GET':
       m = product.objects.filter(id = rid)
       context = {}
       context['data'] = m
       return render(request,"edit.html", context)
   else:
      uname = request.POST['uname']
     
      uprice = request.POST['uprice']
     
      udetail = request.POST['udetail']
     
      ucategory = request.POST['ucategory']

      img = request.FILES['uimage']

      m = product.objects.filter(id = rid)

      

      m.update(name = uname, price = uprice, details = udetail, category = ucategory, image = img)

      return redirect('/dashboard')


def register(request):
   if request.method =="GET":
      return render(request,'register.html')
   else:
       uname = request.POST['uname']
     
       uemail = request.POST['uemail']
     
       upassword = request.POST['upassword']
     
       uconfirmpassword = request.POST['uconfirmpassword']
     
       if uname == "" or upassword == "" or uconfirmpassword == "":
          context = {} #empty dictionary
          context['msg'] = 'fields cannot be empty'

          return render(request,'register.html',context)
       
       elif upassword != uconfirmpassword:
          context = {}
          context['msg'] = 'password and confirm password should be same '
          return render(request,'register.html',context)
       else:
          u = User.objects.create(username = uname, email = uemail)

          u.set_password(upassword)

          u.save()
          context ={}
          context['msg']="user register succesfully"

          return render(request,'register.html',context)




def index(request):
    obj=product.objects.all()

    return render(request,'index.html',{'data':obj})

def about(request):
    return render(request, 'about.html')

def user_login(request):
   if request.method == "GET":
    return render(request, 'login.html')
   else:
      uname = request.POST['uname']

      upassword = request.POST['upassword']

      u = authenticate(username = uname, password = upassword)
      #u me user ka sara informaation save hai.
      if u is not None:
         login(request, u)
         return redirect('/')
      else:
         return HttpResponse("user not found")

def user_logout(request):
   logout(request)
   return redirect('/')   

def addproduct(request):
   m = product.objects.all()
   context = {}

   context['data'] = m
       
   return render(request,'index.html', context)



@login_required
def place_order(request,pid):
    data={}
    if request.method == 'POST':
            quantity = request.POST['quantity']
            obj = product.objects.filter(id=int(pid))
            print(obj[0].price)
            total_price = quantity*obj[0].price
            u=User.objects.filter(id=request.user.id)
            print('user:',u[0].id)
            # Create a new order
            o=Order.objects.create(
                user=u[0],
                product=obj[0],
                quantity=quantity,
                total_price=total_price,
                status='pending'
            )
            o.save()

            print("Order created successfully!")  # Check if order is created

            # messages.success(request, 'Order placed successfully!')
            data={'msg':"Order placed successfully"}
            # return redirect('dashboard')  # Redirect to a success page
            return render(request, 'place_order.html', data)
    else:
        form = OrderForm()
        data['form']=form
    return render(request, 'place_order.html', data)


def view_orders(request):
    # Retrieve order data
    orders = Order.objects.all()

    context = {
        'orders': orders,
    }

    return render(request, 'view_orders.html', context)




def view_order_status(request):
    # Retrieve order status data
    orders = Order.objects.all()

    context = {
        'orders': orders,
    }

    return render(request, 'order_status.html', context)


