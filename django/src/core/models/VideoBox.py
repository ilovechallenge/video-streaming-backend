from django.db import models
from .CategoryBox import CategoryBox
from .GradeBox import GradeBox
from .UnitBox import UnitBox


class VideoBox(models.Model):
    video_id = models.AutoField(primary_key=True,
                                db_column='video_id')
    title = models.CharField(max_length=30,
                             default="No Title",
                             db_column='title')
    content = models.CharField(max_length=200,
                               default="No Content",
                               db_column='content')
    media_url = models.FileField(max_length=200,
                                 default="",
                                 db_column='media_url')
    caption_url = models.FileField(max_length=200,
                                   default="",
                                   db_column='caption_url')
    hls_url = models.CharField(max_length=300,
                               default="",
                               db_column='hls_url')
    category = models.ForeignKey(CategoryBox,
                                 on_delete=models.CASCADE,
                                 db_column='category')
    grade = models.ForeignKey(GradeBox,
                              on_delete=models.CASCADE,
                              db_column='grade')
    unit = models.ForeignKey(UnitBox,
                             on_delete=models.CASCADE,
                             db_column='unit')
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='updated_at')

    def __str__(self):
        return f'{self.video_id} - {self.title}'

    class Meta:
        db_table = 'video_box'
        verbose_name_plural = 'Video Boxes'
