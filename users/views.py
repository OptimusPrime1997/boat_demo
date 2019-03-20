# -*- coding: UTF-8 -*-
# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
from django.utils.encoding import force_text, python_2_unicode_compatible
import json
from users.models import Cargo_Card
from users.models import Tonnage_Card
from users.models import TC_Card
from django.views.decorators.csrf import csrf_exempt


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
        user = TC_Card.objects.filter(Account__contains=content)
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
        user = Cargo_Card.objects.filter(Cargo_name__contains=content)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


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
        user = Tonnage_Card.objects.filter(Vessel_name__contains=content)
        # print(user.toJSON())
        # response['list'] = json.loads(serializers.serialize("json", users))
        response['list'] = json.loads(serializers.serialize("json", user))
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as  e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
