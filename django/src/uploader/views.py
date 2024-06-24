# import time
# from django.shortcuts import render
# from rest_framework import viewsets, parsers, status
# from core.models import (
#     VideoBox,
#     CategoryBox,
#     GradeBox,
#     UnitBox,
#     WordBox,
#     StampBox
# )
# from .serializers import (
#     VideoBoxSerializer,
#     CategoryBoxSerializer,
#     GradeBoxSerializer,
#     UnitBoxSerializer,
#     WordBoxSerializer,
#     StampBoxSerializer
# )
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from django.db import OperationalError
# from django.conf import settings
#
#
# class VideoBoxViewset(viewsets.ModelViewSet):
#     queryset = VideoBox.objects.all()
#     serializer_class = VideoBoxSerializer
#
#     def list(request, *args, **kwargs):
#         queryset = VideoBox.objects.all()
#         serialized_data = []
#
#         for video in queryset:
#             serialized_video = {
#                 'id': video.id,
#                 'title': video.title,
#                 'content': video.content,
#                 'hls_url': video.hls_url,
#                 'media': video.media.url,
#                 'caption': video.caption.url,
#                 'category': video.category.name,
#                 'grade': video.grade.level,  # Get the grade name
#                 'unit': video.unit.name,  # Get the unit name
#                 'created_at': video.created_at,
#             }
#             serialized_data.append(serialized_video)
#
#         return Response(serialized_data)
#
#
# class CategoryBoxViewset(viewsets.ModelViewSet):
#     queryset = CategoryBox.objects.all()
#     serializer_class = CategoryBoxSerializer
#     parser_classes = [parsers.JSONParser]
#     http_method_names = ['get', 'post', 'patch', 'delete']
#
#
# class WordBoxViewset(viewsets.ViewSet):
#     queryset = WordBox.objects.all()
#     serializer_class = WordBoxSerializer
#
#     def list(self, request):
#         video_id = request.query_params.get('video_id')
#         queryset = WordBox.objects.filter(video_id=video_id)
#         serializer = WordBoxSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class StampBoxViewset(viewsets.ViewSet):
#     queryset = StampBox.objects.all()
#     serializer_class = StampBoxSerializer
#
#     def create(self, request):
#         video_id = request.data.get('video_id')
#         best_stamps = request.data.getlist('best_stamps')
#         good_stamps = request.data.getlist('good_stamps')
#         normal_stamps = request.data.getlist('normal_stamps')
#         question = request.data.get('question')
#
#         new_object = StampBox.objects.create(video_id=video_id, best_stamps=best_stamps,
#                                              good_stamps=good_stamps, normal_stamps=normal_stamps, question=question)
#         serializer = StampBoxSerializer(new_object)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class GradeBoxViewset(viewsets.ViewSet):
#     queryset = GradeBox.objects.all()
#     serializer_class = GradeBoxSerializer
#
#     def list(self, request):
#         category_id = request.query_params.get('category_id')
#         queryset = GradeBox.objects.filter(category_id=category_id)
#         serializer = GradeBoxSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['get'])
#     def get_grade_id(self, request):
#         level = request.query_params.get('level')
#         category_id = request.query_params.get('category_id')
#         try:
#             grade = GradeBox.objects.get(level=level, category_id=category_id)
#             grade_id = grade.id
#             return Response({'grade_id': grade_id})
#         except GradeBox.DoesNotExist:
#             return Response({'error': 'GradeBox not found'})
#
#
# class UnitBoxViewset(viewsets.ModelViewSet):
#     queryset = UnitBox.objects.all()
#     serializer_class = UnitBoxSerializer
#
#     def list(self, request):
#         grade_id = request.query_params.get('grade_id')
#         queryset = UnitBox.objects.filter(grade_id=grade_id)
#         serializer = UnitBoxSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['post'])
#     def update_units(self, request):
#         unit_ids = request.data.get('ids', [])
#         for index, unit_id in enumerate(unit_ids, start=1):
#             try:
#                 unit = UnitBox.objects.get(id=unit_id)
#                 unit.order = index
#                 unit.save()
#             except OperationalError as e:
#                 return Response({'error': 'OperationalError', 'message': str(e)}, status=500)
#         return Response({'message': 'success'})
