from rest_framework import viewsets, parsers, status
from rest_framework.decorators import action
from core.models import GradeBox
from ..serializers import GradeBoxSerializer


class GradeBoxViewset(viewsets.ModelViewSet):
    queryset = GradeBox.objects.all()
    serializer_class = GradeBoxSerializer

