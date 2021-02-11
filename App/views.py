from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test



@login_required
def index(request):
    material_count=models.Material.objects.all().count()
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_list = models.Material.objects.all()
    product_list = models.Product.objects.all()
    return render(request, 'index.html', {'material_list': material_list,
    'product_list': product_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})



@login_required
def search(request):
    material_count=models.Material.objects.all().count()
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    if request.method=="POST":
        search = request.POST['q']
        if search:
            match = models.Material.objects.filter(Q(name__icontains=search) | Q(code__icontains=search))
            if match:
                return render(request,'search.html', {'sr': match,
                'material_count': material_count,
                'product_count': product_count,
                'category_count': category_count,
                'supplier_count': supplier_count})
            else:
                messages.error(request,  '   قطعه مورد نظر یافت نشد ، لطفا مجددا جستجو کنید  ' )
        else:
            return HttpResponseRedirect("{% url 'AppBom:search' %}")
    return render(request, 'search.html', {'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})





############### material ###############

@login_required
def material(request):
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()
    material_list = models.Material.objects.all()
    products = models.Product.objects.all()
    categorys = models.Category.objects.all()
    suppliers = models.Supplier.objects.all()
    return render(request, 'material.html', {'material_list': material_list,
    'material_count': material_count,
    'products': products,
    'categorys': categorys,
    'suppliers': suppliers,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})


@login_required
def material_response(request):
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()

    products = models.Product.objects.all()
    categorys = models.Category.objects.all()
    suppliers = models.Supplier.objects.all()
    query = request.GET.get('product')
    products_material = models.Material.objects.filter(product__name=query)
    query = request.GET.get('supplier')
    suppliers_material = models.Material.objects.filter(supplier__name=query)
    query = request.GET.get('category')
    categorys_material = models.Material.objects.filter(category__name=query)
    query = request.GET.get('code')
    codes_material = models.Material.objects.filter(code=query)
    return render(request, 'material_response.html', {'products_material': products_material,
    'suppliers_material': suppliers_material,
    'categorys_material': categorys_material,
    'codes_material': codes_material,
    'products': products,
    'categorys': categorys,
    'suppliers': suppliers,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})


@login_required
def material_detail(request, id):
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()

    material_list = models.Material.objects.all()
    material_detail = get_object_or_404(models.Material, id=id)
    return render(request, 'material_detail.html', {'material_detail': material_detail,
    'material_list': material_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})





############### product ###############

@login_required
def product(request):
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()

    product_list = models.Product.objects.all()
    return render(request, 'product.html', {'product_list': product_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})



@login_required
def product_response(request):
    product_list = models.Product.objects.all()

    material_count=models.Material.objects.all().count()
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    if request.method=="POST":
        search = request.POST['q']
        if search:
            match = models.Product.objects.filter(Q(name__icontains=search) | Q(code__icontains=search))
            if match:
                return render(request,'product_response.html', {'sr': match,
                'product_list': product_list,
                'material_count': material_count,
                'product_count': product_count,
                'category_count': category_count,
                'supplier_count': supplier_count})
            else:
                messages.error(request,  'محصول مورد نظر یافت نشد ، لطفا مجددا جستجو کنید' )
        else:
            return HttpResponseRedirect("{% url 'AppBom:product_response' %}")
    return render(request, 'product_response.html', {'product_list': product_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})



@login_required
def product_detail(request, id):
    material_count=models.Material.objects.all().count()
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()

    product_detail = get_object_or_404(models.Product, id=id)
    products_material = models.Material.objects.filter(product__name=product_detail)
    return render(request, 'product_detail.html', {'product_detail': product_detail,
    'products_material': products_material,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})




############### category ###############

@login_required
def category(request):
    product_count=models.Product.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()
    category_count=models.Category.objects.all().count()

    category_list = models.Category.objects.all()
    return render(request, 'category.html', {'category_list': category_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})


@login_required
def category_response(request):
    category_list = models.Category.objects.all()

    material_count=models.Material.objects.all().count()
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    if request.method=="POST":
        search = request.POST['q']
        if search:
            match = models.Category.objects.filter(Q(name__icontains=search))
            if match:
                return render(request,'category_response.html', {'sr': match,
                'category_list': category_list,
                'material_count': material_count,
                'product_count': product_count,
                'category_count': category_count,
                'supplier_count': supplier_count})
            else:
                messages.error(request,  ' تامین کننده مورد نظر یافت نشد ، لطفا مجددا جستجو کنید' )
        else:
            return HttpResponseRedirect("{% url 'App:category_response' %}")
    return render(request, 'category_response.html', {'category_list': category_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})


@login_required
def category_detail(request, id):
    product_count=models.Product.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()
    category_count=models.Category.objects.all().count()

    category_detail = get_object_or_404(models.Category, id=id)
    category_material = models.Material.objects.filter(category__name=category_detail)
    return render(request, 'category_detail.html', {'category_detail': category_detail,
    'category_material': category_material,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})






############### supplier ###############

@user_passes_test(lambda u: u.is_superuser)
def supplier(request):
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()

    supplier_list = models.Supplier.objects.all()
    superusers = User.objects.filter(is_superuser=True)
    return render(request, 'supplier.html', {'supplier_list': supplier_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})



@user_passes_test(lambda u: u.is_superuser)
def supplier_response(request):
    supplier_list = models.Supplier.objects.all()

    material_count=models.Material.objects.all().count()
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    if request.method=="POST":
        search = request.POST['q']
        if search:
            match = models.Supplier.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
            if match:
                return render(request,'supplier_response.html', {'sr': match,
                'supplier_list': supplier_list,
                'material_count': material_count,
                'product_count': product_count,
                'category_count': category_count,
                'supplier_count': supplier_count})
            else:
                messages.error(request,  ' تامین کننده مورد نظر یافت نشد ، لطفا مجددا جستجو کنید' )
        else:
            return HttpResponseRedirect("{% url 'AppBom:supplier_response' %}")
    return render(request, 'supplier_response.html', {'supplier_list': supplier_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})



@user_passes_test(lambda u: u.is_superuser)
def supplier_detail(request, id):
    material_count=models.Material.objects.all().count()
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()

    supplier_detail = get_object_or_404(models.Supplier, id=id)
    supplier_material = models.Material.objects.filter(supplier__name=supplier_detail)
    return render(request, 'supplier_detail.html', {'supplier_detail': supplier_detail,
    'supplier_material': supplier_material,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})
    
    



############### purchase ###############

@login_required
def foreign_purchase(request):
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()
    f_material_list = models.Material.objects.filter(foreign_purchase=True)
    return render(request, 'foreign_purchase.html', {'f_material_list': f_material_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})



@login_required
def standard_purchase(request):
    product_count=models.Product.objects.all().count()
    category_count=models.Category.objects.all().count()
    supplier_count=models.Supplier.objects.all().count()
    material_count=models.Material.objects.all().count()
    s_material_list = models.Material.objects.filter(standard_purchase=True)
    return render(request, 'standard_purchase.html', {'s_material_list': s_material_list,
    'material_count': material_count,
    'product_count': product_count,
    'category_count': category_count,
    'supplier_count': supplier_count})
