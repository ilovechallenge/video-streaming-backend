from rest_framework import serializers
from core.models import VideoBox


class VideoBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBox
        fields = '__all__'
