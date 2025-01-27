# Generated by Django 4.2.8 on 2024-01-23 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stamphistory',
            name='i_see_stamp_1',
        ),
        migrations.RemoveField(
            model_name='stamphistory',
            name='i_see_stamp_2',
        ),
        migrations.RemoveField(
            model_name='stamphistory',
            name='i_see_stamp_3',
        ),
        migrations.RemoveField(
            model_name='stamphistory',
            name='want_to_know_stamp_1',
        ),
        migrations.RemoveField(
            model_name='stamphistory',
            name='want_to_know_stamp_2',
        ),
        migrations.RemoveField(
            model_name='stamphistory',
            name='want_to_know_stamp_3',
        ),
        migrations.RemoveField(
            model_name='stamphistory',
            name='want_to_tell_stamp_1',
        ),
        migrations.RemoveField(
            model_name='stamphistory',
            name='want_to_tell_stamp_2',
        ),
        migrations.RemoveField(
            model_name='stamphistory',
            name='want_to_tell_stamp_3',
        ),
        migrations.AddField(
            model_name='stamphistory',
            name='i_see_stamp',
            field=models.TextField(db_column='i_see_stamp', default='[]'),
        ),
        migrations.AddField(
            model_name='stamphistory',
            name='want_to_know_stamp',
            field=models.TextField(db_column='want_to_know_stamp', default='[]'),
        ),
        migrations.AddField(
            model_name='stamphistory',
            name='want_to_tell_stamp',
            field=models.TextField(db_column='want_to_tell_stamp', default='[]'),
        ),
    ]
