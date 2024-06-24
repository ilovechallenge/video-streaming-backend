import uuid
from django.db import models
from .VideoBox import VideoBox


class StampBox(models.Model):
    stamp_id = models.UUIDField(primary_key=True,
                                default=uuid.uuid4,
                                editable=False,
                                db_column='stamp_id')
    video = models.ForeignKey(VideoBox,
                              on_delete=models.CASCADE,
                              null=True)
    best_stamps = models.TextField(null=True,
                                   blank=True,
                                   db_column='best_stamps')
    good_stamps = models.TextField(null=True,
                                   blank=True,
                                   db_column='good_stamps')
    normal_stamps = models.TextField(null=True,
                                     blank=True,
                                     db_column='normal_stamps')
    question = models.CharField(max_length=500,
                                null=True,
                                blank=True,
                                db_column='question')
    user_id = models.CharField(max_length=32,
                               null=True,
                               blank=True,
                               db_column='user_id')
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='updated_at')

    def __str__(self):
        return f'{self.stamp_id} - {self.question} - {self.user_id}'

    class Meta:
        db_table = 'stamp_box'
        verbose_name_plural = 'Stamp Boxes'
