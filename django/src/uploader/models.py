# import uuid
# from django.db import models


# Category
# class CategoryBox(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'category_box'
#         verbose_name_plural = 'Category Boxes'


# Grade
# class GradeBox(models.Model):
#     level = models.CharField(max_length=20)
#     category = models.ForeignKey(CategoryBox,
#                                  on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'grade_box'
#         verbose_name_plural = 'Grade Boxes'


# Unit
# class UnitBox(models.Model):
#     name = models.CharField(max_length=100)
#     grade = models.ForeignKey(GradeBox,
#                               on_delete=models.CASCADE)
#     content = models.CharField(max_length=1000,
#                                null=True)
#     is_classic = models.BooleanField(default=False)
#     classic_type = models.CharField(max_length=30,
#                                     null=True)
#     order = models.IntegerField(null=True)
#
#     class Meta:
#         db_table = 'unit_box'
#         verbose_name_plural = 'Unit Boxes'


# Video
# class VideoBox(models.Model):
#     title = models.CharField(max_length=30)
#     content = models.CharField(max_length=200)
#     media = models.FileField(max_length=200,
#                              default="")
#     caption = models.FileField(max_length=200,
#                                default="")
#     hls_url = models.CharField(max_length=300,
#                                default="")
#     category = models.ForeignKey(CategoryBox,
#                                  on_delete=models.CASCADE)
#     grade = models.ForeignKey(GradeBox,
#                               on_delete=models.CASCADE)
#     unit = models.ForeignKey(UnitBox,
#                              on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'video_box'
#         verbose_name_plural = 'Video Boxes'


# Word
# class WordBox(models.Model):
#     id = models.UUIDField(primary_key=True,
#                           default=uuid.uuid4,
#                           editable=False)
#     video = models.ForeignKey(VideoBox,
#                               on_delete=models.CASCADE)
#     word_id = models.IntegerField(null=True)
#     word_text = models.CharField(max_length=100,
#                                  null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'word_box'
#         verbose_name_plural = 'Word Boxes'


# Stamp
# class StampBox(models.Model):
#     id = models.UUIDField(primary_key=True,
#                           default=uuid.uuid4,
#                           editable=False)
#     video = models.ForeignKey(VideoBox,
#                               on_delete=models.CASCADE,
#                               null=True)
#     best_stamps = models.TextField(null=True,
#                                    blank=True)
#     good_stamps = models.TextField(null=True,
#                                    blank=True)
#     normal_stamps = models.TextField(null=True,
#                                      blank=True)
#     question = models.CharField(max_length=500,
#                                 null=True,
#                                 blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'stamp_box'
#         verbose_name_plural = 'Stamp Boxes'
