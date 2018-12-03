from rest_framework import routers, serializers, viewsets
from .models import  Book




class Bookserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name','price',)