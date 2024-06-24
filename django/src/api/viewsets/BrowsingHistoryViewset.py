from rest_framework import viewsets
from core.models import BrowsingHistory
from ..serializers import BrowsingHistorySerializer


class BrowsingHistoryViewset(viewsets.ModelViewSet):
    queryset = BrowsingHistory.objects.all()
    serializer_class = BrowsingHistorySerializer

    def get_queryset(self):
        queryset = BrowsingHistory.objects.all()

        filter_kwargs = {}

        # クエリパラメータをループして条件を構築
        for param in ['user_id', 'browsing_history_id', 'video_id']:
            value = self.request.query_params.get(param)
            if value:
                filter_kwargs[param] = value

        queryset = queryset.filter(**filter_kwargs)
        return queryset
