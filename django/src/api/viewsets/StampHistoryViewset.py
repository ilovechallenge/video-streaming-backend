from rest_framework import viewsets
from core.models import StampHistory
from ..serializers import StampHistorySerializer


class StampHistoryViewset(viewsets.ModelViewSet):
    queryset = StampHistory.objects.all()
    serializer_class = StampHistorySerializer

