from django.db import models
from .CategoryBox import CategoryBox


class GradeBox(models.Model):
    grade_id = models.AutoField(primary_key=True,
                                db_column='grade_id')
    grade = models.CharField(max_length=20,
                             db_column='grade')
    grade_japanese = models.CharField(max_length=20,
                                      db_column='grade_japanese')
    category = models.ForeignKey(CategoryBox,
                                 on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='updated_at')

    def __str__(self):
        return f'{self.grade_id} - {self.grade}'

    class Meta:
        db_table = 'grade_box'
        verbose_name_plural = 'Grade Boxes'
