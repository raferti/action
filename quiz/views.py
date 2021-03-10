from django.shortcuts import render
from django.views.generic import ListView

from quiz.models import Quiz


class QuizListView(ListView):
    model = Quiz
    context_object_name = 'quizzes'
    template_name = 'quiz/quiz_list.html'

