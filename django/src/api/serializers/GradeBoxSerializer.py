from rest_framework import serializers
from core.models import GradeBox


class GradeBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeBox
        fields = '__all__'
