from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .serializers import Bookserializer
from .models import Book


class BookView(APIView):
    @staticmethod
    def get(request):
        items = Book.objects.all()
        return Response(Bookserializer(items, many=True).data)

    @staticmethod
    def post(request):
        item = Book(book_name =request.data["book_name"], price=request.data["price"]).save()
        return Response(Bookserializer(item).data)




