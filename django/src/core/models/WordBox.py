import uuid
from django.db import models
from .VideoBox import VideoBox


class WordBox(models.Model):
    word_id = models.UUIDField(primary_key=True,
                               default=uuid.uuid4,
                               editable=False,
                               db_column='word_id')
    video = models.ForeignKey(VideoBox,
                              on_delete=models.CASCADE,
                              null=True,
                              db_column='video')
    word = models.CharField(max_length=100,
                            null=True,
                            db_column='word'),
    user_id = models.CharField(max_length=32,
                               null=True,
                               db_column='user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.word_id} - {self.word} - {self.user_id}'

    class Meta:
        db_table = 'word_box'
        verbose_name_plural = 'Word Boxes'
