from django.contrib import admin
from . import models

from django.contrib.admin.models import LogEntry
admin.site.register(LogEntry)


admin.site.site_header= "  پنل مدیریت BOM "
admin.site.site_title= "Tavankar"


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
class SupplierAdmin(admin.ModelAdmin):
	list_display = ('name','description')
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','image_tag','description')
class MaterialAdmin(admin.ModelAdmin):
	list_display = ('name','image_tag')
class RateAdmin(admin.ModelAdmin):
	list_display = ('rate','product')


admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Supplier,SupplierAdmin)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Material,MaterialAdmin)
admin.site.register(models.Rate,RateAdmin)
