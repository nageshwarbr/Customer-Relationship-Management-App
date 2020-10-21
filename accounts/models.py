from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (('Indoor', 'Indoor'), ('Outdoor', 'Outdoor'))

    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(max_length=10)
    category = models.CharField(max_length=200, choices=CATEGORY)
    description = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_DEFAULT,default='')
    product=models.ForeignKey(Product,on_delete=models.SET_DEFAULT,default='',null=True)
    STATUS = (('Order pending', 'Order Pending'), ('Out for delivery',
                                                   'Out for delivery'), ('Delivered', 'Delivered'))
    date_created =  models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)
    
