from django.contrib.auth.models import User
from django.test import TestCase

from quiz.models import Quiz, Question, Answer


class QuizListTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('user1', 'mail@mail.ru', '123')
        self.quiz = Quiz.objects.create(name='Опрос 1', user=self.user)
        self.question = Question.objects.create(text='Вопрос 1', quiz=self.quiz)
        self.answer = Answer.objects.create(text='Да', is_correct=True, question=self.question)

    def test_uses_blog_list_template(self):
        """Тест: страница использует шаблон. """
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/quiz_list.html')





