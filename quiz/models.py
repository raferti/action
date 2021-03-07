from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    """Тест"""
    name = models.CharField('Имя', max_length=70)
    update_at = models.DateTimeField('Обновленно', auto_now=True)
    create_at = models.DateTimeField('Созданно', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    """Вопросы теста"""
    text = models.CharField('Вопрос', max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f'{self.text[:10]}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Ответы на вопросы"""
    text = models.CharField('Ответ', max_length=250)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f'{self.text[:10]}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
