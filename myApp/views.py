import struct

from django.http import JsonResponse, HttpResponse
from django.core import serializers

from myApp.models import UserInfo
import json


def add_userInfo(request):
    response = {}
    try:
        userInfo = UserInfo(user_name=request.GET.get('user_name'),
                            user_password=request.GET.get('user_password'),
                            user_type=request.GET.get('user_type'))
        userInfo.save()
        response['msg'] = 'success'
        response['userId'] = userInfo.id
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def search_userInfo(request):
    response = {}
    try:
        userInfo = UserInfo.objects.get(user_name=request.GET.get('user_name'),
                                        user_password=request.GET.get('user_password'))
        response['userId'] = userInfo.id
        response['user_type'] = userInfo.user_type
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def search_usertype(request):
    response = {}
    try:
        userInfo = UserInfo.objects.get(id=request.GET.get('user_id'))

        response['user_type'] = userInfo.user_type
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def fetch_userInfo(request):
    response = {}
    try:
        userInfo = UserInfo.objects.get(id=request.GET.get('user_id'))
        userInfoss = UserInfo.objects.filter(id=request.GET.get('user_id'))
        response['user_name'] = userInfo.user_name if userInfo.user_name else ""
        response['user_mobile'] = userInfo.user_mobile if userInfo.user_mobile else ""
        response['user_avatar'] = json.loads(serializers.serialize("json", userInfoss))[0]
        response['user_address'] = userInfo.user_address if userInfo.user_address else ""
        response['user_createtime'] = str(userInfo.user_createtime)
        response['user_province'] = userInfo.user_province if userInfo.user_province else ""
        response['user_city'] = userInfo.user_city if userInfo.user_city else ""
        response['user_area'] = userInfo.user_area if userInfo.user_area else ""
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def edit_userInfo(request):
    response = {}
    global userInfo
    print("111")
    iid=int(str(request.FILES.get('user_id').read())[2:-1])

    try:
        print(iid)
        userInfo = UserInfo.objects.get(id=iid)
        print(iid)

        save_userInfo = json.loads(request.FILES.get('forms').read())
        same_name = UserInfo.objects.filter(user_name=save_userInfo['user_name'])
        if(same_name.count()==2):
            response['msg'] = "用户名重复"
            response['error_num'] = 1
            return JsonResponse(response)
        elif same_name.count()==1:
            if str(same_name[0].id)!=str(iid):
                print("name1:",str(same_name[0].id))
                print("name2:", str(iid))
                response['msg'] = "用户名重复"
                response['error_num'] = 1
                return JsonResponse(response)

        userInfo.user_name=save_userInfo['user_name']
        userInfo.user_address=save_userInfo['user_address']
        userInfo.user_mobile=save_userInfo['user_mobile']

        if request.FILES.get('user_image'):
            userInfo.user_avatar=request.FILES.get('user_image')

        save_addrInfo = json.loads(request.FILES.get('selectAddr').read())
        userInfo.user_province=save_addrInfo['province']
        userInfo.user_city=save_addrInfo['city']
        userInfo.user_area=save_addrInfo['area']

        userInfo.save()

        response['image'] = str(userInfo.user_avatar)
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def userId2userName(request):
    response = {}
    try:
        userInfo = UserInfo.objects.get(id=request.GET.get('user_id'))
        response['user_name'] = userInfo.user_name
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def edit_password(request):
    response = {}
    try:
        userInfo = UserInfo.objects.filter(id=request.GET.get('user_id'),user_password=request.GET.get('old_password'))
        if(userInfo.count()==0):
            response['msg'] = 'succes111s'
            response['error_num'] = -1

        else:
            u=userInfo[0]
            u.user_password=request.GET.get('new_password')
            u.save()
            response['msg'] = 'succes111s'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
