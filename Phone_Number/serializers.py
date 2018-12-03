from rest_framework import routers, serializers, viewsets

from .models import Phone


class PhonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ('name', 'tel','img')
