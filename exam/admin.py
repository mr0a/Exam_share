from django.contrib import admin
from .models import *

# Register your models here.
model_list = [Exam, Part, Question, Option, Upvote]
admin.site.register(model_list)

class OptionInline(admin.TabularInline):
    model = Option

class UpvotesInline(admin.TabularInline):
    model = Upvote

class QuestionAdmin(admin.ModelAdmin):
    inlines=[
        OptionInline, UpvotesInline
    ]