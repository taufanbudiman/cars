from django.contrib import admin

from .models import CarBrand

# Register your models here.
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ["code", "desc"]
    readonly_fields = ["created_date", "updated_date"]
    fields = ["code", "desc", "created_by", "updated_by"] + readonly_fields
    

admin.site.register(CarBrand, CarBrandAdmin)

