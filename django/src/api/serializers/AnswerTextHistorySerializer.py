import json
from rest_framework import serializers
from core.models import AnswerTextHistory


class StrokeField(serializers.Field):
    def to_representation(self, value):
        value = value.replace('"', '')
        return json.loads(value)

    def to_internal_value(self, data):
        return json.dumps(data)


class AnswerTextHistorySerializer(serializers.ModelSerializer):
    stroke = StrokeField()

    class Meta:
        model = AnswerTextHistory
        fields = [
            'answer_text_history_id',
            'stroke',
            'stroke_text',
            'keyboard_text',
            'browsing_history',
            'delete_flg',
            'created_at',
            'updated_at',
        ]
