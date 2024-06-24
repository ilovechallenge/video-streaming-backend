from rest_framework import serializers
from core.models import StampHistory


class StampTimeListField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        response_list = [str(item).replace(' ', '').replace("'", "").replace('"', '')
                         for item in data.replace('[', '').replace(']', '').split(',')]

        if not isinstance(response_list, list):
            raise serializers.ValidationError("This field must be a list.")
        if not all(isinstance(item, str) for item in response_list):
            raise serializers.ValidationError("All items must be string.")

        return response_list


class StampHistorySerializer(serializers.ModelSerializer):
    want_to_know_stamp = StampTimeListField()
    i_see_stamp = StampTimeListField()
    want_to_tell_stamp = StampTimeListField()

    class Meta:
        model = StampHistory
        fields = [
            'stamp_history_id',
            'browsing_history',
            'want_to_know_stamp',
            'i_see_stamp',
            'want_to_tell_stamp',
            'delete_flg',
            'created_at',
            'updated_at'
        ]
