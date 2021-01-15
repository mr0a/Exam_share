from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from . import models
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from django.views import View



# Create your views here.
def index(req):
    if req.user.is_authenticated:
        exams = models.Exam.objects.all()
        return render(req, template_name='exam/index.html', context={'exams': exams})
    return render(req, template_name='exam/index.html')

class ExamView(View):
    def get(self, req, exam_id):
        parts = models.Part.objects.filter(Exam=exam_id)
        exam = models.Exam.objects.filter(id=exam_id)[0]
        return render(req, 'exam/exam.html', context={'parts': parts, 'exam': exam })

    def post(self, req, exam_id):
        if req.POST.get('answer'):
            answer_option = models.Option(title=req.POST.get('answer'), question_id = req.POST.get('question_id'), answered_by_id = req.user.id)
            answer_option.save()
            return JsonResponse({'success': True})

        if req.POST.get('question'):
            question = models.Question(title=req.POST.get('question'), part_id=req.POST.get('part_id'))
            question.save()
            return JsonResponse({'success': True})


def questions(req, part_id):
    questions = models.Question.objects.filter(part=part_id).values_list('id', 'title')
    return JsonResponse({'questions': list(questions) })

def myfun(x):
    return x['upvotes']

def options(req, question_id):
    options = list(models.Option.objects.filter(question = question_id).values('id', 'title', 'answered_by_id'))
    for option in options:
        user_id = option['answered_by_id']
        user = SocialAccount.objects.filter(user_id=user_id).values()
        user = list(user)
        # print(user[0]['extra_data']['picture'])
        option['answered_by_id'] = user[0]['extra_data']['picture']
        upvotes = models.Upvote.objects.filter(option_id=option['id'])
        upvoted = models.Upvote.objects.filter(option_id=option['id'], user_id=req.user.id)
        option['upvotes'] = len(upvotes)
        option['upvoted'] = True if len(upvoted) != 0 else False
    options.sort(key=myfun, reverse=True)
    return JsonResponse({'options': options})


def vote(req, option_id):
    vote, created = models.Upvote.objects.get_or_create(option_id = option_id, user = req.user)
    question = models.Option.objects.filter(id=option_id).values('question_id')[0]['question_id']
    if created:
        return JsonResponse({'created': True, 'id': question})
    vote.delete()
    return JsonResponse({'created': False, 'id': question})
    