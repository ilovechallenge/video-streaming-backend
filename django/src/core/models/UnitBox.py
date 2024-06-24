from django.db import models
from .GradeBox import GradeBox


class UnitBox(models.Model):
    unit_id = models.AutoField(primary_key=True,
                               db_column='unit_id')
    unit = models.CharField(max_length=100,
                            db_column='unit')
    grade = models.ForeignKey(GradeBox,
                              on_delete=models.CASCADE,
                              db_column='grade')
    content = models.CharField(max_length=1000,
                               null=True,
                               db_column='content')
    is_classic = models.BooleanField(default=False,
                                     db_column='is_classic')
    classic_type = models.CharField(max_length=30,
                                    null=True,
                                    db_column='classic_type')
    order = models.IntegerField(null=True,
                                db_column='order')
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='updated_at')

    def __str__(self):
        return f'{self.unit_id} - {self.unit}'

    class Meta:
        db_table = 'unit_box'
        verbose_name_plural = 'Unit Boxes'
