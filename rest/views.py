from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .serializers import ItemSerializer
from .models import Item


class ItemView(APIView):
    @staticmethod
    def get(request):
        items = Item.objects.all()
        return Response(ItemSerializer(items, many=True).data)

    @staticmethod
    def post(request):
        item = Item(title=request.data["title"], body=request.data["body"]).save()
        return Response(ItemSerializer(item).data)
