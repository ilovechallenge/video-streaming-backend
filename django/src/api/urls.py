from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .viewsets import (
    VideoBoxViewset,
    CategoryBoxViewset,
    GradeBoxViewset,
    UnitBoxViewset,
    WordBoxViewset,
    StampBoxViewset,
    BrowsingHistoryViewset,
    StampHistoryViewset,
    AnswerTextHistoryViewset,
)
from .views import (
    CheckBrowsingHistoryView,
)

router = SimpleRouter()
router.register('videos', VideoBoxViewset, basename='videos')
router.register('categories', CategoryBoxViewset, basename='categories')
router.register('grades', GradeBoxViewset, basename='grades')
router.register('units', UnitBoxViewset, basename='units')
router.register('words', WordBoxViewset, basename='words')
router.register('stamps', StampBoxViewset, basename='stamps')
router.register('browsing-history', BrowsingHistoryViewset, basename='browsing-history')
router.register('stamp-history', StampHistoryViewset, basename='stamp-history')
router.register('answer-text-history', AnswerTextHistoryViewset, basename='answer-text-history')

urlpatterns = [
    path('', include(router.urls)),
    path('check-browsing-history/', CheckBrowsingHistoryView.as_view(), name='check-browsing-history')
]
