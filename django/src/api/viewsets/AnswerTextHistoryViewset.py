from rest_framework import viewsets
from core.models import AnswerTextHistory
from ..serializers import AnswerTextHistorySerializer


class AnswerTextHistoryViewset(viewsets.ModelViewSet):
    queryset = AnswerTextHistory.objects.all()
    serializer_class = AnswerTextHistorySerializer

