from django.contrib import admin

from quiz.models import Quiz, Question, Answer


@admin.register(Quiz)
class AdminQuiz(admin.ModelAdmin):
    fields = ('name', 'user')


@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    fields = ('text',)


@admin.register(Answer)
class AdminAnswer(admin.ModelAdmin):
    fields = ('text', 'is_correct', 'question')

