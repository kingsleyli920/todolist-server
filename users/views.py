from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsersSerializer
from .models import Users
import json
import uuid
from datetime import datetime


# Create your views here.
class UsersSignUp(APIView):
    def get(self, request):
        data = UsersSerializer(Users.objects.all(), many=True).data
        res = {
            'success': True,
            'data': data
        }
        return Response(res)

    def post(self, request):
        data = json.loads(request.body)
        data['id'] = uuid.uuid1()
        data['registered_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Users.objects.create(**data)
        res = {
            'success': True,
            'data': data
        }
        return Response(res)

# Create your views here.
class UsersLogin(APIView):
    def get(self, request):
        data = UsersSerializer(Users.objects.all(), many=True).data
        res = {
            'success': True,
            'data': data
        }
        return Response(res)

    def post(self, request):
        query_list = Users.objects.all()
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        if username and password:
            query_list = query_list.filter(username__exact=username)
            query_list = query_list.filter(password__exact=password)
        else :
            query_list = []
        query_list = UsersSerializer(query_list, many=True).data
        res = {
            'success': True,
            'data': query_list
        }
        return Response(res)
