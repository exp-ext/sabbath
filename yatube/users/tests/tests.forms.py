from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class UserFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.signup = reverse('users:signup')
        cls.index = reverse('posts:index')

    def setUp(self):
        self.guest_client = Client()

    def test_user_create(self):
        """Валидная форма создает нового пользователя."""
        form_data = {
            'first_name': 'Test name',
            'last_name': 'Test surname',
            'username': 'Test username',
            'email': 'test@email.done',
            'password1': 'SamiySlojniyPassHaHaHa',
            'password2': 'SamiySlojniyPassHaHaHa',
        }

        response = self.authorized_client.post(
            UserFormTests.signup,
            data=form_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, UserFormTests.index)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
