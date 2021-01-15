# Generated by Django 3.1.3 on 2021-01-15 03:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0007_auto_20210114_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='upvotes',
            field=models.ManyToManyField(related_name='option_upvotes', through='exam.Upvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together={('option', 'user')},
        ),
    ]