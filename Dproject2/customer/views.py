from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic import View, TemplateView
from Admin.models import Item, ItemSubCategory, ItemCategory
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView
from django.db.models import Avg, Max, Min, Sum

from rest_framework.views import APIView
from rest_framework.response import Response

import random

from django.template import loader


# Create your views here.
product = []

class IndexView(TemplateView):
    template_name = 'LandingPage.html'

@csrf_exempt
def subcategories(request):
    global product
    category = request.POST.get('category','')
    selected_category = ItemCategory.objects.get(category_name = category)
    product = ItemSubCategory.objects.filter(category = selected_category.id)
    return HttpResponse()


@csrf_exempt
def helper(request):
    return render(request, 'helper.html', context = {'data':product})


def products(request, category):
    response_list = []
    sub_category_id = ItemSubCategory.objects.get(sub_category_name = category).id
    distinct_id_products = Item.objects.filter(sub_category_id= sub_category_id).values('ItemId').distinct()
    for products in distinct_id_products:
        items = []
        same_itemid = Item.objects.filter(ItemId=products['ItemId'])
        max = same_itemid.aggregate(Max('price_per_unit'))['price_per_unit__max']
        for item in same_itemid:
            if item.price_per_unit == max:
                items.insert(0, item)
            else:
                items.append({'item_upc' : item.item_upc, 'unit' :item.unit})
        response_list.append(items)
    return render(request, 'products.html', context={'products':response_list})


@csrf_exempt
def get_price(request):
    print('hello')
    upc = request.POST.get('item_upc','')
    item = Item.objects.get(item_upc=upc)
    data = {'market_price' : item.market_price, 'unit' : item.unit, 'price': item.price_per_unit}
    return HttpResponse(json.dumps(data))

# @csrf_exempt
# def filter(request):
#     category = request.POST.get('id', '')
#     response_list = []
#     if category == 'all':
#         distinct_id_products = Item.objects.all(sub_category_id= sub_category_id).values('ItemId').distinct()
#     else:
#         category_id = ItemCategory.objects.get(category_name = category).id
#         distinct_id_products = Item.objects.filter(category=category_id).values('ItemId').distinct()
#
#     for products in distinct_id_products:
#         items = []
#         same_itemid = Item.objects.filter(ItemId=products['ItemId'])
#         max = same_itemid.aggregate(Max('price_per_unit'))['price_per_unit__max']
#         for item in same_itemid:
#             if item.price_per_unit == max:
#                 items.insert(0, item)
#             else:
#                 items.append({'item_upc' : item.item_upc, 'unit' :item.unit})
#         response_list.append(items)
#     print(response_list)
#     return HttpResponse(json.dumps(response_list))

phone_otp = {}

class sendOtp(APIView):

    def post(self,request,format=None):
        phoneNumber = request.data["phone_no"]
        if phoneNumber:
            phone = str(phoneNumber)
            key = sendOtpToPhone(phone)
            if key:
                phone_otp[str(phone)] = str(key)
                print(phone_otp)
                return Response({
                    'error' : 'false',
                    'message' : 'OTP sent'
                })

        else:
            return Response({
                'error' : 'true',
                'message' : 'Mobile Number not found'
            })
            
class verifyOtp(APIView):

    def post(self,request,format=None):
        print(request.data)
        phoneNumber = request.data["phone_no"]
        otpRecieved = request.data["otp"]
        if phoneNumber:
            phone = str(phoneNumber)
            otp = str(otpRecieved)
            if phone:
                if phone in phone_otp.keys():
                    if otp:
                        realOtp = phone_otp[str(phone)]
                        if realOtp == otp:
                            del phone_otp[str(phone)]
                            return Response({
                                'error' : 'false',
                                'message' : 'OTP Valid'
                            })
                        else:
                            del phone_otp[str(phone)]
                            return Response({
                                'error' : 'true',
                                'message' : 'OTP invalid'
                            })
                        print(phone_otp)

                    else:
                        return Response({
                            'error' : 'true',
                            'message' : 'OTP not entered'
                        })

                else:
                    return Response({
                        'error' : 'true',
                        'message' : 'OTP not present for the mobile number'
                    })

        else:
            return Response({
                'error' : 'true',
                'message' : 'Mobile Number not entered'
            })


def sendOtpToPhone(phone):
    if phone:
        key = random.randint(999,9999)
        print(key)
        return key
    else:
        return False