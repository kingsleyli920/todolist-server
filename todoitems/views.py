from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ToDoItemSerializer
from .models import ToDoItem
from users.models import Users
import json
import uuid
from django.utils import timezone
from users.serializers import UsersSerializer
from datetime import datetime
from rest_framework import status


# Create your views here.
class List(APIView):
    def get(self, request):
        get = request.GET
        print request.GET
        getOrderOpt = int(get['orderOpt'])
        getPage = get['page']
        getUserId = str(get['userId'])
        data = ToDoItem.objects.order_by(('updated_time')).reverse()
        if getOrderOpt is 1:
            data = ToDoItem.objects.order_by(('priority')).reverse()
            print '1'
        elif getOrderOpt is 2:
            data = ToDoItem.objects.order_by(('priority'))
            print '2'
        elif getOrderOpt is 3:
            data = ToDoItem.objects.order_by(('expired_date'))
            print '3'
        elif getOrderOpt is 4:
            data = ToDoItem.objects.order_by(('expired_date')).reverse()
            print '4'
        elif getOrderOpt is 5:
            data = ToDoItem.objects.order_by(('start_date'))
            print '5'
        elif getOrderOpt is 6:
            data = ToDoItem.objects.order_by(('start_date')).reverse()
            print '6'
        elif getOrderOpt is 7:
            data = ToDoItem.objects.order_by(('status'))
            print '7'

        data = data.filter(userId__exact=getUserId)
        length = len(data)
        if len(data) == 0:
            res = {
                'success': False,
                'data': [],
                'length': 0
            }
            return Response(res)
        startIdx = (int(getPage) - 1) * 3
        endIdx = int(getPage) * 3
        data = data[startIdx:endIdx]
        for item in data:
            itemData = ToDoItemSerializer(item).data
            curItemExpiredTime = itemData['expired_date']
            if curItemExpiredTime < str(timezone.now()) and itemData['status'] is 0:
                curItem = ToDoItem.objects.all().filter(id__exact=itemData['id']).filter(status__exact=0)
                curItem.update(status=2)

        data = ToDoItemSerializer(data, many=True).data
        # print data
        res = {
            'success': True,
            'data': data,
            'length': length
        }
        return Response(res)

    def post(self, request):
        data = json.loads(request.body)
        curUser = Users.objects.get(id__exact=data['userId'])
        data['id'] = uuid.uuid1()
        data['updated_time'] = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        data['userId'] = curUser
        obj = ToDoItem.objects.create(**data)
        if obj is not None:
            d = {
                'success': True,
            }
        else:
            d = {
                'success': False,
            }
        return Response(d)

    def delete(self, request):
        data = json.loads(request.body)
        print data
        curItem = ToDoItem.objects.get(id__exact=data['id'])
        if curItem is not None:
            curItem.delete()
            data = {
                'success': True
            }
            return Response(data)
        else:
            data = {
                'success': False
            }
            return Response(data)


# Create your views here.
class Item(APIView):
    def get(self, request):
        get = request.GET
        itemId = get['id']
        item = ToDoItem.objects.get(id__exact=itemId)
        if item is not None:
            returnedItem = ToDoItemSerializer(item).data
            data = {
                'item': returnedItem,
                'success': True
            }
            return Response(data)
        else:
            data = {
                'success': True
            }
            return Response(data)

    def put(self, request):
        data = request.data
        id = data['id']
        del data['id']
        data['updated_time'] = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        item = ToDoItem.objects.all().filter(id__exact=id)
        rows = item.update(**data)
        if rows > 0:
            data = {
                'success': True
            }
            return Response(data)
        data = {
            'success': False
        }
        return Response(data)
