from django.urls import path

from quiz.views import QuizListView


urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
]
