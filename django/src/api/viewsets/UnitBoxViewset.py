from rest_framework import viewsets, parsers, status
from rest_framework.decorators import action
from core.models import UnitBox
from ..serializers import UnitBoxSerializer


class UnitBoxViewset(viewsets.ModelViewSet):
    queryset = UnitBox.objects.all()
    serializer_class = UnitBoxSerializer
