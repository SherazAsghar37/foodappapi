from django.contrib import admin
from api.models import Food,Products,CustomUser
admin.register(Food)
admin.site.register(CustomUser)
class FoodAdmin(admin.ModelAdmin):
    list_display=('total_size','type_id','offset')
class ProductsAdmin(admin.ModelAdmin):
    list_display=('id','name','description','price','stars','img','location','created_at','updated_at','type_id')
# Register your models here.
