from rest_framework import serializers
from core.models import WordBox


class WordBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordBox
        fields = '__all__'
