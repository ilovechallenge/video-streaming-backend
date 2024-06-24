import uuid
from django.db import models
from .BrowsingHistory import BrowsingHistory


class StampHistory(models.Model):
    stamp_history_id = models.UUIDField(primary_key=True,
                                        default=uuid.uuid4,
                                        editable=False,
                                        db_column='stamp_history_id')
    browsing_history = models.ForeignKey(BrowsingHistory,
                                         on_delete=models.CASCADE)
    want_to_know_stamp = models.TextField(default='[]',
                                          db_column='want_to_know_stamp')
    i_see_stamp = models.TextField(default='[]',
                                   db_column='i_see_stamp')
    want_to_tell_stamp = models.TextField(default='[]',
                                          db_column='want_to_tell_stamp')
    delete_flg = models.BooleanField(default=False,
                                     db_column='delete_flg')
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='updated_at')

    def __str__(self):
        return f'{self.stamp_history_id} - {self.browsing_history.browsing_history_id} - {self.browsing_history.user_id}'

    class Meta:
        db_table = 'stamp_history'
        verbose_name_plural = 'Stamp History'
