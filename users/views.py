# -*- coding: UTF-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json



from users.models import Cargo_Card
from users.models import Tonnage_Card
from users.models import TC_Card
import datetime
from django.db.models import Q

DWT_ARRAY = [0, 10000, 40000, 35000, 40000, 50000, 65000]


# tonnage_card
@csrf_exempt
@require_http_methods(["GET"])
def get_tonnage(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        user = Tonnage_Card.objects.all().order_by('-Sent')
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
        user = Tonnage_Card.objects.filter(Vessel_name__icontains=content).order_by('-Sent')
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
        user = Tonnage_Card.objects.filter(Open_date_S__icontains=content, Open_date_E__icontains=content).order_by('-Sent')
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
        user = Cargo_Card.objects.all().order_by('-Sent')
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
        user = Cargo_Card.objects.filter(Cargo_name__icontains=content).order_by('-Sent')
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
        user = TC_Card.objects.all().order_by('-Sent')
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
        user = TC_Card.objects.filter(Account__icontains=content).order_by('-Sent')
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


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

#  tonnage 搜索方法
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
        dwt2 = request_body['dwt2']
        open_area = request_body['open_area']


        # BLT应该为int型，容易比较大小
        # datetime.date(int(opendate_start[0:4]), int(opendate_start[5:7]),
        #               int(opendate_start[8:10])
        #               )
        # .filter(Vessel_name__icontains='A') \
        # '2018-03-08'

        day=datetime.datetime.now().date()-datetime.timedelta(days=days-1)
        day_from=str(datetime.datetime(day.year, day.month, day.day, 0, 0, 0))
        timeArray = time.strptime(day_from, "%Y-%m-%d %H:%M:%S")
        otherStyleTime = time.strftime("%Y/%-m/%-d %H:%M", timeArray)


        print(otherStyleTime)
        # q1 = Tonnage_Card.objects.filter(BLT__gte=datetime.datetime.now().year-built)
        q1 = Tonnage_Card.objects.filter(Q(Vessel_name__icontains=vessel_name),

                                         Q(Open_area__icontains=open_area),
                                         Q(DWT__gte=dwt,DWT__lte=dwt2),
                                         Q(Sent__gte=otherStyleTime),
                                         Q(BLT__gte=datetime.datetime.now().year-built),
                                         Q(Q(
                                            Q(Open_date_S__gte=datetime.date(int(opendate_start[0:4]), int(opendate_start[5:7]),
                                                int(opendate_start[8:10]))),
                                            Q(Open_date_E__lte=datetime.date(int(opendate_end[0:4]),
                                                int(opendate_end[5:7]),int(opendate_end[8:10])))
                                            )|
                                           Q(
                                            Q(Open_date_S__lte=datetime.date(int(opendate_end[0:4]), int(opendate_end[5:7]),
                                                int(opendate_end[8:10]))),
                                            Q(Open_date_S__gte=datetime.date(int(opendate_start[0:4]),
                                                int(opendate_start[5:7]),int(opendate_start[8:10])))
                                            )|
                                           Q(
                                            Q(Open_date_E__lte=datetime.date(int(opendate_end[0:4]), int(opendate_end[5:7]),
                                                int(opendate_end[8:10]))),
                                            Q(Open_date_E__gte=datetime.date(int(opendate_start[0:4]),
                                                int(opendate_start[5:7]),int(opendate_start[8:10])))
                                            )

                                           ),
                                         # BLT__gte=datetime.datetime.today().year-int(built),
                                         # BLT__lte= datetime.datetime.today().year ,

                                         ).order_by('-Sent')

        # if dwt!="":
        #     q2=q1.filter(DWT_gt=dwt,)


        list = [vessel_name, sender_mail, opendate_start, opendate_end, days, built, account, dwt,open_area,dwt2]
        print(list)
        print(json.loads(serializers.serialize("json", q1)))
        response['list'] = json.loads(serializers.serialize("json", q1))
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)


#  cargo 搜索方法

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

        day = datetime.datetime.now().date() - datetime.timedelta(days=days - 1)
        day_from = str(datetime.datetime(day.year, day.month, day.day, 0, 0, 0))
        timeArray = time.strptime(day_from, "%Y-%m-%d %H:%M:%S")
        otherStyleTime = time.strftime("%Y/%-m/%-d %H:%M", timeArray)
        print(otherStyleTime)
        q1 = Cargo_Card.objects.filter(Q(Cargo_name__icontains=cargo_name),

                                       Q(Quantity_s__gte=quantity),
                                       Q(Sent__gte=otherStyleTime),

                                       Q(Q(
                                           Q(LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
                                                                            int(laycan_start[5:7]),
                                                                            int(laycan_start[8:10]))),
                                           Q(LayCan_E__lte=datetime.date(int(laycan_end[0:4]),
                                                                            int(laycan_end[5:7]),
                                                                            int(laycan_end[8:10])))
                                       ) |
                                         Q(
                                             Q(LayCan_S__lte=datetime.date(int(laycan_end[0:4]),
                                                                              int(laycan_end[5:7]),
                                                                              int(laycan_end[8:10]))),
                                             Q(LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
                                                                              int(laycan_start[5:7]),
                                                                              int(laycan_start[8:10])))
                                         ) |
                                         Q(
                                             Q(LayCan_E__lte=datetime.date(int(laycan_end[0:4]),
                                                                              int(laycan_end[5:7]),
                                                                              int(laycan_end[8:10]))),
                                             Q(LayCan_E__gte=datetime.date(int(laycan_start[0:4]),
                                                                              int(laycan_start[5:7]),
                                                                              int(laycan_start[8:10])))
                                         )

                                         ),


                                       ).order_by('-Sent')

        list = [cargo_name, sender_mail, laycan_start, laycan_end, days, quantity, account]
        print(list)

        print(json.loads(serializers.serialize("json", q1)))
        response['list'] = json.loads(serializers.serialize("json", q1))
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)


# tc 搜索方法



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

        day = datetime.datetime.now().date() - datetime.timedelta(days=days - 1)
        day_from = str(datetime.datetime(day.year, day.month, day.day, 0, 0, 0))
        timeArray = time.strptime(day_from, "%Y-%m-%d %H:%M:%S")
        otherStyleTime = time.strftime("%Y/%-m/%-d %H:%M", timeArray)
        print(otherStyleTime)

        q1 = TC_Card.objects.filter(Q(Account__icontains=acc),
                                    Q(Quantity_s__gte=quantity),
                                    Q(Sent__gte=otherStyleTime),

                                    Q(Q(
                                        Q(LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
                                                                      int(laycan_start[5:7]),
                                                                      int(laycan_start[8:10]))),
                                        Q(LayCan_E__lte=datetime.date(int(laycan_end[0:4]),
                                                                      int(laycan_end[5:7]),
                                                                      int(laycan_end[8:10])))
                                    ) |
                                      Q(
                                          Q(LayCan_S__lte=datetime.date(int(laycan_end[0:4]),
                                                                        int(laycan_end[5:7]),
                                                                        int(laycan_end[8:10]))),
                                          Q(LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
                                                                        int(laycan_start[5:7]),
                                                                        int(laycan_start[8:10])))
                                      ) |
                                      Q(
                                          Q(LayCan_E__lte=datetime.date(int(laycan_end[0:4]),
                                                                        int(laycan_end[5:7]),
                                                                        int(laycan_end[8:10]))),
                                          Q(LayCan_E__gte=datetime.date(int(laycan_start[0:4]),
                                                                        int(laycan_start[5:7]),
                                                                        int(laycan_start[8:10])))
                                      )

                                      ),


                                    # LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
                                    #                             int(laycan_start[5:7]),
                                    #                             int(laycan_start[8:10])),
                                    # LayCan_E__lte=datetime.date(int(laycan_end[0:4]), int(laycan_end[5:7]),
                                    #                             int(laycan_end[8:10])),

                                    ).order_by('-Sent')

        list = [acc, sender_mail, laycan_start, laycan_end, days, quantity, account]
        print(list)

        print(json.loads(serializers.serialize("json", q1)))
        response['list'] = json.loads(serializers.serialize("json", q1))

        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)



# 查找tonnage非完整信息的方法
@csrf_exempt
@require_http_methods(["GET"])
def tonnage_card_incomplete(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # L = [1, '', 0, 'A', "  ", None, [1, 2], False, 3.14, [], {'a': 1}, {}]
        # filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), L)
        # user = Tonnage_Card.objects.filter(Sent="")
        user = Tonnage_Card.objects.filter(Q(Open_area="no open area match")|Q(Sent="")
                                           |Q(Open_date_S="1900-01-01")|Q(Sent="0")).order_by('-Sent')

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

# 查找tonnage完整信息的方法
@csrf_exempt
@require_http_methods(["GET"])
def tonnage_card_complete(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # L = [1, '', 0, 'A', "  ", None, [1, 2], False, 3.14, [], {'a': 1}, {}]
        # filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), L)
        # user = Tonnage_Card.objects.filter(Sent="")
        user = Tonnage_Card.objects.filter(~Q(Open_area="no open area match")&~Q(Sent="")
                                           &~Q(Open_date_S="1900-01-01")&~Q(Sent="0")).order_by('-Sent')

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


# 查找cargo非完整信息的方法
@csrf_exempt
@require_http_methods(["GET"])
def cargo_card_incomplete(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # L = [1, '', 0, 'A', "  ", None, [1, 2], False, 3.14, [], {'a': 1}, {}]
        # filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), L)
        # user = Tonnage_Card.objects.filter(Sent="")
        user = Cargo_Card.objects.filter(Q(Cargo_name="none item name match")|Q(Sent="")
                                           |Q(LayCan_S="1900-01-01")|Q(Sent="0")|
                                            Q(Loading_Port="no loading port match")|
                                          Q(Discharging_Port ="no discharging port match")

                                        ).order_by('-Sent')

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

# 查找cargo完整信息的方法
@csrf_exempt
@require_http_methods(["GET"])
def cargo_card_complete(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # L = [1, '', 0, 'A', "  ", None, [1, 2], False, 3.14, [], {'a': 1}, {}]
        # filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), L)
        # user = Tonnage_Card.objects.filter(Sent="")
        user = Cargo_Card.objects.filter(~Q(Cargo_name="none item name match")&~Q(Sent="")
                                           &~Q(LayCan_S="1900-01-01")&~Q(Sent="0")&~
                                            Q(Loading_Port="no loading port match")&~
                                          Q(Discharging_Port ="no discharging port match").order_by('-Sent')

        )

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


# 查找tc非完整信息的方法
@csrf_exempt
@require_http_methods(["GET"])
def tc_card_incomplete(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # L = [1, '', 0, 'A', "  ", None, [1, 2], False, 3.14, [], {'a': 1}, {}]
        # filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), L)
        # user = Tonnage_Card.objects.filter(Sent="")
        user = TC_Card.objects.filter(Q(Account="no account match")|Q(Sent="")
                                           |Q(LayCan_S="1900-01-01")|Q(Sent="0")|
                                            Q(Delivery_area="no dely match")|Q(Delivery_area="none dely match")|
                                            Q(Delivery_area="no delivery area match")|
                                          Q(Redelivery_area ="No redely match")|
                                          Q(Redelivery_area ="none redely match")|
                                          Q(Redelivery_area ="no redelivery area match")|
                                          Q(Quantity_s ="0")|
                                          Q(DUR_S ="0")

                                        ).order_by('-Sent')

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

# 查找tc完整信息的方法
@csrf_exempt
@require_http_methods(["GET"])
def tc_card_complete(request):
    response = {}
    try:
        print("tests:")
        # users = User.objects.filter(email=email)
        # L = [1, '', 0, 'A', "  ", None, [1, 2], False, 3.14, [], {'a': 1}, {}]
        # filter(lambda s: s and (type(s) != str or len(s.strip()) > 0), L)
        # user = Tonnage_Card.objects.filter(Sent="")
        user = TC_Card.objects.filter(~Q(Account="no account match")&~Q(Sent="")
                                      &~Q(LayCan_S="1900-01-01")&~Q(Sent="0")&~
                                            Q(Delivery_area="no dely match")&~
                                            Q(Delivery_area="none dely match")&~
                                            Q(Delivery_area="no delivery area match")&~
                                          Q(Redelivery_area ="No redely match")&~
                                          Q(Redelivery_area ="none redely match")&~
                                          Q(Redelivery_area ="no redelivery area match")&~
                                          Q(Quantity_s ="0")&~
                                          Q(DUR_S ="0")

                                        ).order_by('-Sent')
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




# # tonnage 编辑更新方法
@csrf_exempt
@require_http_methods(["PUT"])
def tonnage_update(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['Vessel_name']
        acc2 = request_body['DWT']
        acc3 = request_body['BLT']
        acc4 = request_body['Open_area']
        acc5 = request_body['Open_date_S']
        acc6 = request_body['Open_date_E']
        acc7 = request_body['Sent']
        acc8 = request_body['ID']
        acc9 = request_body['mail_text']

        tonnage_card = Tonnage_Card(Vessel_name=acc1, DWT=acc2, BLT=acc3, Open_area=acc4, Open_date_S=acc5, Open_date_E=acc6,
                          Sent=acc7,
                          ID=acc8, mail_text=acc9)
        result = tonnage_card.save(force_update=True)


        list = [acc1, acc2, acc3, acc4, acc5, acc6, acc7, acc8, acc9]

        response['result'] = "success"

        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2

    return JsonResponse(response)

# # cargo 编辑更新方法
@csrf_exempt
@require_http_methods(["PUT"])
def cargo_update(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['Cargo_name']
        acc2 = request_body['Quantity_s']
        acc3 = request_body['Quantity_e']
        acc4 = request_body['Loading_Port']
        acc5 = request_body['Discharging_Port']
        acc6 = request_body['LayCan_S']
        acc7 = request_body['LayCan_E']
        acc8 = request_body['Sent']
        acc9 = request_body['ID']
        acc10 = request_body['mail_text']



        cargo_card = Cargo_Card(Cargo_name=acc1, Quantity_s=acc2, Quantity_e=acc3, Loading_Port=acc4, Discharging_Port=acc5, LayCan_S=acc6,
                                LayCan_E=acc7,
                                Sent=acc8, ID=acc9, mail_text=acc10)
        result = cargo_card.save(force_update=True)

        # q1 = TC_Card.objects.filter(Account__icontains=acc,
        #                             Quantity_s__gt=quantity,
        #
        #                             LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
        #                                                         int(laycan_start[5:7]),
        #                                                         int(laycan_start[8:10])),
        #                             LayCan_E__lte=datetime.date(int(laycan_end[0:4]), int(laycan_end[5:7]),
        #                                                         int(laycan_end[8:10])),
        #
        #                             )

        list = [acc1, acc2, acc3, acc4, acc5, acc6, acc7, acc8, acc9, acc10]
        # print(list)
        # print(json.loads(serializers.serialize("json", tc_card)))
        response['result'] = "success"
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)


# # tc 编辑更新方法
@csrf_exempt
@require_http_methods(["PUT"])
def tc_update(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['Account']
        acc2 = request_body['Delivery_area']
        acc3 = request_body['Redelivery_area']
        acc4 = request_body['Sent']
        acc5 = request_body['ID']
        acc6 = request_body['LayCan_E']
        acc7 = request_body['LayCan_S']
        acc8 = request_body['mail_text']
        acc9 = request_body['Quantity_s']
        acc10 = request_body['Quantity_e']
        acc11 = request_body['DUR_S']
        acc12 = request_body['DUR_E']

        tc_card = TC_Card(Account=acc1, Delivery_area=acc2, Redelivery_area=acc3, Sent=acc4, ID=acc5, LayCan_E=acc6,
                          LayCan_S=acc7,
                          mail_text=acc8, Quantity_s=acc9, Quantity_e=acc10, DUR_S=acc11, DUR_E=acc12)
        result = tc_card.save(force_update=True)

        # q1 = TC_Card.objects.filter(Account__icontains=acc,
        #                             Quantity_s__gt=quantity,
        #
        #                             LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
        #                                                         int(laycan_start[5:7]),
        #                                                         int(laycan_start[8:10])),
        #                             LayCan_E__lte=datetime.date(int(laycan_end[0:4]), int(laycan_end[5:7]),
        #                                                         int(laycan_end[8:10])),
        #
        #                             )

        list = [acc1, acc2, acc3, acc4, acc5, acc6, acc7, acc8, acc9, acc10, acc11, acc12]
        # print(list)
        # print(json.loads(serializers.serialize("json", tc_card)))
        response['result'] = "success"
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)

# ton增加星标的方法
@csrf_exempt
@require_http_methods(["PUT"])
def ton_flag(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['ID']
        value=request_body['value']
        Tonnage_Card.objects.filter(ID=acc1).update(flag=value)

        # q1 = TC_Card.objects.filter(Account__icontains=acc,
        #                             Quantity_s__gt=quantity,
        #
        #                             LayCan_S__gte=datetime.date(int(laycan_start[0:4]),
        #                                                         int(laycan_start[5:7]),
        #                                                         int(laycan_start[8:10])),
        #                             LayCan_E__lte=datetime.date(int(laycan_end[0:4]), int(laycan_end[5:7]),
        #                                                         int(laycan_end[8:10])),
        #
        #                             )

        # list = [acc1, acc2, acc3, acc4, acc5, acc6, acc7, acc8, acc9, acc10, acc11, acc12]
        # print(list)
        # print(json.loads(serializers.serialize("json", tc_card)))
        response['result'] = "success"
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)

# cargo增加星标的方法
@csrf_exempt
@require_http_methods(["PUT"])
def cargo_flag(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['ID']
        value=request_body['value']
        Cargo_Card.objects.filter(ID=acc1).update(flag=value)

        response['result'] = "success"
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)

# tc增加星标的方法
@csrf_exempt
@require_http_methods(["PUT"])
def tc_flag(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['ID']
        value=request_body['value']
        TC_Card.objects.filter(ID=acc1).update(flag=value)

        response['result'] = "success"
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)

# ton修改日期方法
@csrf_exempt
@require_http_methods(["PUT"])
def ton_date(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['ID']
        opendate_start=request_body['opendate_start']
        opendate_end=request_body['opendate_end']
        Tonnage_Card.objects.filter(ID=acc1).update(Open_date_S=opendate_start)
        Tonnage_Card.objects.filter(ID=acc1).update(Open_date_E=opendate_end)

        response['result'] = "success"
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)

# cargo修改日期方法
@csrf_exempt
@require_http_methods(["PUT"])
def cargo_date(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['ID']
        laycan_start=request_body['laycan_start']
        laycan_end=request_body['laycan_end']
        Cargo_Card.objects.filter(ID=acc1).update(LayCan_S=laycan_start)
        Cargo_Card.objects.filter(ID=acc1).update(LayCan_E=laycan_end)

        response['result'] = "success"
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)

# tc修改日期方法
@csrf_exempt
@require_http_methods(["PUT"])
def tc_date(request):
    response = {}
    try:
        # get data from POST request
        request_body = json.loads(request.body.decode())
        acc1 = request_body['ID']
        laycan_start=request_body['laycan_start']
        laycan_end=request_body['laycan_end']
        TC_Card.objects.filter(ID=acc1).update(LayCan_S=laycan_start)
        TC_Card.objects.filter(ID=acc1).update(LayCan_E=laycan_end)

        response['result'] = "success"
        response['err_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 2
    return JsonResponse(response)




