from django.db import models
#
#
# class Address(models.Model):
#     address_id = models.AutoField(primary_key=True)
#     street1 = models.CharField(max_length=50)
#     street2 = models.CharField(max_length=50)
#     area = models.CharField(max_length=25)
#     city = models.CharField(max_length=25)
#     landmark = models.CharField(max_length=25)
#     type = models.CharField(max_length=15)
#     def __str__(self):
#         return self.address_id
#
# class DeliveryBoy(models.Model):
#     delivery_boy_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     phone_no = models.CharField(max_length=15)
#     password = models.CharField(max_length=100)
#     lat_long = models.CharField(max_length=30)
#     def __str__(self):
#         return self.delivery_boy_id


class ItemCategory(models.Model):
    id = models.AutoField(primary_key=True, db_column='category_id')
    category_name = models.CharField(max_length=100, db_column='category_name')

    def __str__(self):
        return self.category_name


class ItemSubCategory(models.Model):
    id = models.AutoField(db_column = 'sub_category_id', primary_key=True)
    sub_category_name = models.CharField(max_length=100)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=False, default = None)
    image_path = models.FileField(upload_to='images/')

    def __str__(self):
        return self.sub_category_name


class Item(models.Model):
    item_upc = models.CharField(primary_key=True, max_length=255)
    ItemId = models.IntegerField()
    item_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length= 100, default=None, null=True, blank=True)
    unit = models.CharField(max_length=100)
    price_per_unit = models.FloatField()
    market_price = models.FloatField(default=0.00)
    available_qty = models.IntegerField(default=0)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=False, default = None)
    sub_category = models.ForeignKey(ItemSubCategory, on_delete=models.CASCADE, default=None)
    image_path = models.FileField(upload_to='images/')
    item_description = models.TextField(default=None, null=True, blank=True)
    def __str__(self):
        return self.item_name

#
# class Users(models.Model):
#     cust_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     mobile_no = models.CharField(max_length=10)
#     address = models.CharField(max_length=100)
#     lat_long = models.CharField(max_length=30)
#     def __str__(self):
#         return self.name

#
#
# class Vehicle_Info(models.Model):
#     vehicle_id = models.AutoField(primary_key=True)
#     vehicle_number = models.CharField(max_length=15)
#     type = models.CharField(max_length=20)
#     user_id = models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
#     lat_long = models.CharField(max_length=30)
#     def __str__(self):
#         return self.vehicle_id
#
# class OrderList(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     quantity = models.IntegerField()
#     unit = models.IntegerField()
#     item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.order_id
#
# class UserOrder(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     delivery_location = models.ForeignKey(Address, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
#     order_list = models.ForeignKey(OrderList, on_delete=models.CASCADE)
#     status = models.CharField(max_length=30)
#     def __str__(self):
#         return self.order_id
#
#
# class BufferStock(models.Model):
#     item_id=models.ForeignKey(Item, on_delete=models.CASCADE)
#     delivery_id=models.ForeignKey(Address, on_delete=models.CASCADE)
#     quantity=models.IntegerField()
#
#
# class Order(models.Model):
#     customer_id=models.ForeignKey(Users, on_delete=models.CASCADE)
#     order_id=models.AutoField(primary_key=True)
#     delivery_time=models.DateField(auto_now_add=True)
#     status=models.CharField(max_length=30,default="pending")
#     # item_id=models.ForeignKey(Item, on_delete=models.CASCADE)
#     address_id=models.ForeignKey(Address, on_delete=models.CASCADE)
#     quantity=models.IntegerField()
#     customer_status=models.CharField(max_length=30,default="pending")
#     delivery_boy_status=models.CharField(max_length=30,default="pending")
#     admin_status=models.CharField(max_length=30,default="pending")
#
#     def __str__(self):
#         return self.order_id
#
# class AllotedArea(models.Model):
#     user_id=models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
#     vehicle_id=models.ForeignKey(Vehicle_Info, on_delete=models.CASCADE)
#     area_code=models.CharField(max_length=30)
