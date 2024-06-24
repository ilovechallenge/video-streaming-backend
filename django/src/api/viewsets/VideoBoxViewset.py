from rest_framework import viewsets
from core.models import VideoBox
from ..serializers import VideoBoxSerializer


class VideoBoxViewset(viewsets.ModelViewSet):
    queryset = VideoBox.objects.all()
    serializer_class = VideoBoxSerializer
