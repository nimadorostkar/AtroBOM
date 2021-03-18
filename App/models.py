from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse



class Category(models.Model):
    name=models.CharField(max_length=200,verbose_name = "نام")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('App:category_detail',args=[self.id])



class Supplier(models.Model):
    name=models.CharField(max_length=200,verbose_name = "نام")
    description=models.TextField(max_length=800,null=True, blank=True,verbose_name = "توضیحات")
    phone_number = models.CharField(max_length=50,null=True, blank=True,verbose_name = "شماره تلفن")
    address=models.CharField(max_length=200,null=True, blank=True,verbose_name = "آدرس")
    email=models.CharField(max_length=200,null=True, blank=True,verbose_name = "ایمیل")
    website=models.CharField(max_length=200,null=True, blank=True,verbose_name = "وبسایت")

    class Meta:
        verbose_name = "تامین کننده"
        verbose_name_plural = "تامین کنندگان"
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('App:supplier_detail',args=[self.id])



class Product(models.Model):
    code=models.CharField(max_length=50,null=True, blank=True,verbose_name = "کد ")
    name=models.CharField(max_length=200,verbose_name = "نام")
    description=models.TextField(max_length=800,null=True, blank=True,verbose_name = "توضیحات")
    image=models.ImageField(upload_to='image/product', default='image/Default.png' ,null=True, blank=True,verbose_name = "تصویر")

    class Meta:
        verbose_name = "موارد کاربرد"
        verbose_name_plural = "موارد کاربرد"

    def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.image.url))

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('App:product_detail',args=[self.id])



#------------------------------------------------------------------------
class Rate(models.Model):
    rate=models.CharField(max_length=10,null=True, blank=True,verbose_name = " ضریب مصرف ")
    product=models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name = " موارد کاربرد  ")
    
    def __str__(self):
        return self.product.name + ' ' + self.rate
        
    def get_absolute_url(self):
        return reverse('App:material_detail',args=[self.id])
    
    class Meta:
        verbose_name = " ضریب مصرف"
        verbose_name_plural = " ضرایب مصرف"
        

class Material(models.Model):
    #author=models.ForeignKey(User, on_delete=models.SET_NULL,null=True, default=User.username ,verbose_name = "نویسنده" )
    code=models.CharField(max_length=100,null=True, blank=True,verbose_name = "کد ")
    name=models.CharField(max_length=400,verbose_name = "نام")
    description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات")
    box_description=models.TextField(max_length=500,null=True, blank=True,verbose_name = "مشخصات بسته بندی")
    foreign_purchase=models.BooleanField(default=False,verbose_name = " خرید خارجی ")
    standard_purchase=models.BooleanField(default=False,verbose_name = "  خرید استاندارد ")
    product=models.ManyToManyField(Product,verbose_name = "موارد کاربرد ")
    supplier=models.ManyToManyField(Supplier,verbose_name = "تامین کنند ")
    category=models.ManyToManyField(Category,verbose_name = "دسته بندی ")
    image=models.ImageField(upload_to='image/material',default='image/Default.png',null=True, blank=True,verbose_name = "تصویر قطعه")
    box_img=models.ImageField(upload_to='image/box',default='image/Default.png' ,null=True, blank=True,verbose_name = "تصویر بسته بندی")
    file = models.FileField(upload_to ='uploads',default='uploads/Default.png',null=True, blank=True,verbose_name = "فایل نقشه قطعه") 
    rate = models.ManyToManyField(Rate,null=True, blank=True,verbose_name = " ضریب مصرف  ")
    tag=models.TextField(max_length=500,null=True, blank=True,verbose_name = "برچسب ها ")
    


    class Meta:
        verbose_name = "قطعه"
        verbose_name_plural = "قطعات"

    def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.image.url))

    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('App:material_detail',args=[self.id])
