# Generated by Django 3.1.3 on 2021-01-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20210114_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='title',
            field=models.CharField(default='A', max_length=20),
        ),
    ]