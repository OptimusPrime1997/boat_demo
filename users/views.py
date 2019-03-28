# -*- coding: UTF-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
from users.models import Cargo_Card
from users.models import Tonnage_Card
from users.models import TC_Card
import datetime

DWT_ARRAY = [0, 10000, 40000, 35000, 40000.50000, 65000]


# tonnage_card
@csrf_exempt
@require_http_methods(["GET"])
def get_tonnage(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        user = Tonnage_Card.objects.all()
        print(user)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@csrf_exempt
@require_http_methods(["GET"])
def search_tonnage(request, content):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # user = Cargo_Cards.objects.filter()
        user = Tonnage_Card.objects.filter(Vessel_name__icontains=content)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@csrf_exempt
@require_http_methods(["GET"])
def search_tonnage_data(request, content):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # user = Cargo_Cards.objects.filter()
        user = Tonnage_Card.objects.filter(Open_date_S__icontains=content, Open_date_E__icontains=content)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# cargo_card
@csrf_exempt
@require_http_methods(["GET"])
def get_cargo(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        user = Cargo_Card.objects.all()
        print(user)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        print(serializers.serialize("json", user))
        print(json.loads(serializers.serialize("json", user)))
        response['list'] = json.loads(serializers.serialize("json", user))
        print(response['list'])
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@csrf_exempt
@require_http_methods(["GET"])
def search_cargo(request, content):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # user = Cargo_Cards.objects.filter()
        user = Cargo_Card.objects.filter(Cargo_name__icontains=content)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# tc_card
@csrf_exempt
@require_http_methods(["GET"])
def get_tc(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        user = TC_Card.objects.all()
        print(user)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@csrf_exempt
@require_http_methods(["GET"])
def search_tc(request, content):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # user = Cargo_Cards.objects.filter()
        user = TC_Card.objects.filter(Account__icontains=content)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

#
# {
# 	"vessel_name":"PACIFIC ACE",
# 	"sender_mail":"0",
# 	"opendate_start":"2019-03-02",
# 	"opendate_end":"2019-03-02",
# 	"days":1,
# 	"built":5,
# 	"account":"mouses",
# 	"dwt":0
# }

@csrf_exempt
@require_http_methods(["POST"])
def tonnage_card_search(request):
    response = {}
    try:
        request_body = json.loads(request.body.decode())
        # print("request_body:", request_body)
        vessel_name = request_body['vessel_name']
        print(vessel_name)
        sender_mail = request_body['sender_mail']
        opendate_start = request_body['opendate_start']
        opendate_end = request_body['opendate_end']
        days = request_body['days']
        built = request_body['built']
        account = request_body['account']
        # dwt -1 represent all
        dwt = request_body['dwt']

        # BLT应该为int型，容易比较大小
        # datetime.date(int(opendate_start[0:4]), int(opendate_start[5:7]),
        #               int(opendate_start[8:10])
        #               )
        # .filter(Vessel_name__icontains='A') \
        # '2018-03-08'
        q1 = Tonnage_Card.objects.filter(Vessel_name__icontains=vessel_name,
                                         Open_date_S__gte=datetime.date(int(opendate_start[0:4]), int(opendate_start[5:7]),
                                           int(opendate_start[8:10])) ,
                                         Open_date_E__lte=datetime.date(int(opendate_end[0:4]), int(opendate_end[5:7]),
                                              int(opendate_end[8:10])) ,
                                         BLT__gte=datetime.datetime.today().year-int(built),
                                         BLT__lte= datetime.datetime.today().year ,
        )


        list = [vessel_name, sender_mail, opendate_start, opendate_end, days, built, account, dwt]
        print(list)
        print(json.loads(serializers.serialize("json", q1)))
        response['result'] = json.loads(serializers.serialize("json", q1))
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)

#
# {
# 	"cargo_name":"Coal",
# 	"sender_mail":"0",
# 	"laycan_start":"2018-03-20",
# 	"laycan_end":"2018-03-31",
# 	"days":1,
#   "quantity":0,
# 	"account":"mouses"
#
# }

# to do
@csrf_exempt
@require_http_methods(["POST"])
def cargo_card_search(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        cargo_name = request_body['cargo_name']
        print(cargo_name)
        sender_mail = request_body['sender_mail']
        laycan_start = request_body['laycan_start']
        laycan_end = request_body['laycan_end']
        days = request_body['days']
        quantity = request_body['quantity']
        account = request_body['account']
        q1 = Cargo_Card.objects.filter(Cargo_name__icontains=cargo_name,
                                         LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
                                                                        int(laycan_start[5:7]),
                                                                        int(laycan_start[8:10])),
                                         LayCan_E__lte=datetime.date(int(laycan_end[0:4]), int(laycan_end[5:7]),
                                                                        int(laycan_end[8:10])),

                                         )

        list = [cargo_name , sender_mail, laycan_start, laycan_end, days,quantity, account]
        print(list)

        print(json.loads(serializers.serialize("json", q1)))
        response['result'] = json.loads(serializers.serialize("json", q1))
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)

# {
# 	"acc":"TONGLI TIANJIN",
# 	"sender_mail":"0",
# 	"laycan_start":"2018-03-06",
# 	"laycan_end":"2018-03-10",
# 	"days":1,
#   "quantity":0,
# 	"account":"mouses"
#
# }
# to do
@csrf_exempt
@require_http_methods(["POST"])
def tc_card_search(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc = request_body['acc']
        print(acc)
        sender_mail = request_body['sender_mail']
        laycan_start = request_body['laycan_start']
        laycan_end = request_body['laycan_end']
        days = request_body['days']
        quantity = request_body['quantity']
        account = request_body['account']
        q1 = TC_Card.objects.filter(Account__icontains=acc,
                                       LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
                                                                   int(laycan_start[5:7]),
                                                                   int(laycan_start[8:10])),
                                       LayCan_E__lte=datetime.date(int(laycan_end[0:4]), int(laycan_end[5:7]),
                                                                   int(laycan_end[8:10])),

                                       )

        list = [acc, sender_mail, laycan_start, laycan_end, days, quantity, account]
        print(list)

        print(json.loads(serializers.serialize("json", q1)))
        response['result'] = json.loads(serializers.serialize("json", q1))
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)