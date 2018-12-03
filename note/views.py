from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .serializers import NoteSerializer
from .models import Note


class NoteView(APIView):
    @staticmethod
    def get(request):
        items = Note.objects.all()
        return Response(NoteSerializer(items, many=True).data)

    @staticmethod
    def post(request):
        item = Note(note=request.data["note"]).save()
        return Response(NoteSerializer(item).data)
