from rest_framework import viewsets, parsers, status
from core.models import CategoryBox
from ..serializers import CategoryBoxSerializer


class CategoryBoxViewset(viewsets.ModelViewSet):
    queryset = CategoryBox.objects.all()
    serializer_class = CategoryBoxSerializer
