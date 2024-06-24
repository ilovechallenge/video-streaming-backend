from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from core.models import BrowsingHistory
from ..serializers import BrowsingHistorySerializer


class CheckBrowsingHistoryView(views.APIView):

    def get(self, request):
        user_id = request.query_params.get('user_id')
        video_id = request.query_params.get('video_id')

        if not user_id or not video_id:
            return Response({"error": "user_id and video_id are required."}, status=status.HTTP_400_BAD_REQUEST)

        browsing_history = BrowsingHistory.objects.filter(user_id=user_id, video_id=video_id).first()

        if not browsing_history:
            browsing_history = BrowsingHistory.objects.create(**filter_kwargs)

        serializer = BrowsingHistorySerializer(browsing_history)

        return Response(serializer.data)
