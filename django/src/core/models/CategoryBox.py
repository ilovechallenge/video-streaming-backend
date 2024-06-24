from django.db import models


class CategoryBox(models.Model):
    category_id = models.AutoField(primary_key=True,
                                   db_column='category_id')
    category = models.CharField(max_length=50,
                                db_column='category')
    category_japanese = models.CharField(max_length=50,
                                         db_column='category_japanese')
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='updated_at')

    def __str__(self):
        return f'{self.category_id} - {self.category}'

    class Meta:
        db_table = 'category_box'
        verbose_name_plural = 'Category Boxes'
