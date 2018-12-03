from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from  .serializers import PhonSerializer

from .models import Phone


class PhoneView(APIView):
    @staticmethod
    def get(request):
        itmes = Phone.objects.all();
        return  Response(PhonSerializer(itmes,many=True).data)


    @staticmethod
    def post(request):
        item = Phone(name=request.data['name'],tel=request.data['tel'],img=request.data['img']).save()
        return Response(PhonSerializer(item).data)

