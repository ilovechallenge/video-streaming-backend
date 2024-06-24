import uuid
from django.db import models
from .VideoBox import VideoBox


class BrowsingHistory(models.Model):
    browsing_history_id = models.UUIDField(primary_key=True,
                                           default=uuid.uuid4,
                                           editable=False,
                                           db_column='browsing_history_id')
    video = models.ForeignKey(VideoBox,
                              on_delete=models.CASCADE,
                              null=True)
    user_id = models.CharField(max_length=32,
                               null=True,
                               blank=True,
                               db_column='user_id')
    delete_flg = models.BooleanField(default=False,
                                     db_column='delete_flg')
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='updated_at')

    def __str__(self):
        return f'{self.browsing_history_id} - {self.user_id} - {self.video}'

    class Meta:
        db_table = 'browsing_history'
        verbose_name_plural = 'Browsing History'
