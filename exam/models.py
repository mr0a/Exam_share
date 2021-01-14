from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exam(models.Model):
    title = models.fields.CharField(max_length=30)
    date = models.fields.DateField()

    def __str__(self) -> str:
        return self.title


class Part(models.Model):
    Exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    title = models.fields.CharField(max_length=20, default='Part A')

    def __str__(self):
        return f'{str(self.Exam_id)} {self.title}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Exam_id', 'title'], name='unique_part_exam')
        ]

class Question(models.Model):
    title = models.TextField()
    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.part} {self.id}'

class Option(models.Model):
    title = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Q {self.question} by {self.answered_by}'

class Upvote(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)