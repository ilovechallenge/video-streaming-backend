import uuid
from django.db import models
from .BrowsingHistory import BrowsingHistory


class AnswerTextHistory(models.Model):
    answer_text_history_id = models.UUIDField(primary_key=True,
                                              default=uuid.uuid4,
                                              editable=False,
                                              db_column='answer_text_history_id')
    stroke = models.TextField(null=True,
                              blank=True,
                              db_column='stroke')
    stroke_text = models.TextField(null=True,
                                   blank=True,
                                   db_column='stroke_text')
    keyboard_text = models.TextField(null=True,
                                     blank=True,
                                     db_column='keyboard_text')
    browsing_history = models.ForeignKey(BrowsingHistory,
                                         on_delete=models.CASCADE)
    delete_flg = models.BooleanField(default=False,
                                     db_column='delete_flg')
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='updated_at')

    def __str__(self):
        return f'{self.answer_text_history_id} - {self.browsing_history.browsing_history_id} - {self.browsing_history.user_id}'

    class Meta:
        db_table = 'answer_text_history'
        verbose_name_plural = 'Answer Text History'
