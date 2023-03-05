# Generated by Django 3.2 on 2022-12-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20221130_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='selected_extra_courses',
            field=models.ManyToManyField(to='course.ExtraCourse'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_extra',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='extracourse',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='extracourse',
            name='selected',
        ),
    ]