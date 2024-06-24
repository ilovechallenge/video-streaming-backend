from rest_framework import viewsets
from core.models import WordBox
from ..serializers import WordBoxSerializer


class WordBoxViewset(viewsets.ModelViewSet):
    queryset = WordBox.objects.all()
    serializer_class = WordBoxSerializer

