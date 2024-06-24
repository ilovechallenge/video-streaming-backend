from rest_framework import serializers
from core.models import CategoryBox


class CategoryBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryBox
        fields = '__all__'
