from rest_framework import viewsets, parsers, status
from rest_framework.decorators import action
from core.models import StampBox
from ..serializers import StampBoxSerializer


class StampBoxViewset(viewsets.ModelViewSet):
    queryset = StampBox.objects.all()
    serializer_class = StampBoxSerializer
