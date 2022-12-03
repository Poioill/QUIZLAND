from django.shortcuts import render
from django.views.generic import DetailView
from .models import Answers, Quiz_links, Quiz_items


def index(request):
    return render(request, 'index.html', {'answers': Answers.objects.all(), 'quizlinks': Quiz_links.objects.all()})


class QuizDetailView(DetailView):
    model = Quiz_items
    context_object_name = 'quizzes'
    slug_field = 'quiz_detail'


'''
def math(request):
    return render(request, 'math.html')


def lit(request):
    return render(request, 'literature.html')


def geo(request):
    return render(request, 'geo.html')


def science(request):
    return render(request, 'science.html')


def lang(request):
    return render(request, 'languages.html')

def basic(request):
    return render(request, 'basic.html')
    '''
