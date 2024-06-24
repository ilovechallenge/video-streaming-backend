from rest_framework import serializers
from core.models import UnitBox


class UnitBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitBox
        fields = '__all__'
