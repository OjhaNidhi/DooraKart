from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *
# Register your models here.
# admin.site.register(Address)
# admin.site.register(AllotedArea)
# admin.site.register(BufferStock)
# admin.site.register(DeliveryBoy)
# admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(ItemSubCategory)
# admin.site.register(Users)
# admin.site.register(Vehicle_Info)
# admin.site.register(OrderList)
# admin.site.register(UserOrder)
# admin.site.register(Order)




class ItemResource(resources.ModelResource):

    class Meta:
        model = Item
        exclude = ('image_path', )
        import_id_fields = ['item_upc']

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource
