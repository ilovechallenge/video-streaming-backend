from rest_framework import serializers
from core.models import StampBox


class StampBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = StampBox
        fields = '__all__'
