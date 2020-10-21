from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm
from django.forms import inlineformset_factory
from .filter import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Acount created successfully for '+user)
            return redirect('login')
    context={'form':form}
    return render(request,'accounts/register.html',context)


def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all().order_by('-date_created')[:5]
    total_orders = Order.objects.all().count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending_orders = Order.objects.filter(status='Order pending').count()
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders, 'delivered': delivered, 'pending_orders': pending_orders}
    return render(request, 'accounts/dashboard.html',context)


def product(request):
    products=Product.objects.all()
    return render(request, 'accounts/profile.html',{'products':products})


def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    myFilter=OrderFilter(request.GET,queryset=orders,)
    orders=myFilter.qs
    context = {'customer': customer , 'orders': orders
               , 'total_orders': total_orders, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html',context)
    
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'),extra=1)


    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
            #print('Printing POST:', request.POST)
            #form = OrderForm(request.POST)
            formset = OrderFormSet(request.POST, instance=customer)
            if formset.is_valid():
                formset.save()
                return redirect('/')

    context = {'form': formset}
    return render(request, 'accounts/orderform.html', context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/orderform.html', context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
