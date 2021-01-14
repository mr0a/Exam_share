from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from . import models
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount



# Create your views here.
def index(req):
    if req.user.is_authenticated:
        exams = models.Exam.objects.all()
        return render(req, template_name='exam/index.html', context={'exams': exams})
    return render(req, template_name='exam/index.html')

@login_required
def exam_part(req, exam_id):
    if req.GET.get('answer'):
        answer_option = models.Option(title=req.GET.get('answer'), question_id = req.GET.get('question_id'), answered_by_id = req.user.id)
        # answer_option.answered_by = req.user.id
        print(req.user)
        print(answer_option)
        answer_option.save()
        return redirect('exam', exam_id=exam_id)
    parts = models.Part.objects.filter(Exam=exam_id)
    exam = models.Exam.objects.filter(id=exam_id)[0]
    return render(req, 'exam/exam.html', context={'parts': parts, 'exam': exam })


def questions(req, part_id):
    questions = models.Question.objects.filter(part=part_id).values_list('id', 'title')
    return JsonResponse({'questions': list(questions) })

def options(req, question_id):
    options = list(models.Option.objects.filter(question = question_id).values('title', 'answered_by_id'))
    for option in options:
        user_id = option['answered_by_id']
        user = SocialAccount.objects.filter(user_id=user_id).values()
        user = list(user)
        # print(user[0]['extra_data']['picture'])
        option['answered_by_id'] = user[0]['extra_data']['picture']
    return JsonResponse({'options': options})
    