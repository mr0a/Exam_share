# Generated by Django 3.1.3 on 2021-01-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]