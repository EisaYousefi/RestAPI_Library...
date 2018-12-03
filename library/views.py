from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .serializers import BooksSerializer,Azoserializer,AmanatSerializer
from .models import Books, Azo, Amanat


# class BooksView(APIView):
#     @staticmethod
#     def get(request):
#         items = Books.objects.all()
#         return Response(BooksSerializer(items, many=True).data)
#

    # @staticmethod
    # def post(request):
    #     item = Books(id  =request.data["id"],
    #                  bookName=request.data["bookName"],
    #                  authorName=request.data["authorName"],
    #                  publishers=request.data["publishers"],
    #                  price=request.data["price"]).save()
    #     return Response(BooksSerializer(item).data)



    #Azo class

# class AzoView(APIView):
#     @staticmethod
#     def get(request):
#         items = Azo.objects.all()
#         return Response(AzoSerializer(items , many= True).data)
#
#
#
#
#
#     @staticmethod
#     def post(request):
#         item = Azo(id_azo    = request.data["id_azo"],
#                    nameFamil = request.data["nameFamil"],
#                    tel       = request.data["tel"]
#         ).save()
#         return  Response(AzoSerializer(item).data)





class BookViewset(viewsets.ModelViewSet):
    queryset =Books.objects.all();
    serializer_class =BooksSerializer

class AzoViewset(viewsets.ModelViewSet):
    queryset = Azo.objects.all()
    serializer_class = Azoserializer



class AmanatViewset(viewsets.ModelViewSet):
    queryset = Amanat.objects.all()
    serializer_class = AmanatSerializer



