from rest_framework import serializers
from core.models import BrowsingHistory


class BrowsingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrowsingHistory
        fields = '__all__'
