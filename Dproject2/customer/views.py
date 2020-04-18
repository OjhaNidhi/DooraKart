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
