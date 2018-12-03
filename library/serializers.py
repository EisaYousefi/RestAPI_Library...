from rest_framework import routers, serializers, viewsets
from .models import Books, Azo, Amanat


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('id','bookName','authorName','publishers','price', )


class Azoserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Azo
        fields = ("id_azo","nameFamil","tel")



class AmanatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Amanat
        fields = ("name_book_amanat","id_book_amanat","writername_book_amanat","tel_amanat","name_amanat","id_name_amanat")