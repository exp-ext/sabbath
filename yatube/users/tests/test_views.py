from django import forms
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class UsersViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='auth',
            password="12345",
            phone_number='+722988776655'
        )
        cls.password_change_form = reverse('users:password_change_form')
        cls.logout = reverse('users:logout')
        cls.login = reverse('users:login')
        cls.signup = reverse('users:signup')
        cls.password_reset_done = reverse('users:password_reset_done')
        cls.password_reset_form = reverse('users:password_reset_form')
        # cls.password_reset_confirm = reverse(
        #     'users:password_reset_confirm',
        #     kwargs={'uidb64': '?',
        #             'token': '?'}
        # )
        cls.password_reset_complete = reverse('users:password_reset_complete')

    def setUp(self):
        self.guest_client = Client()

        self.authorized_client = Client()
        self.authorized_client.force_login(UsersViewsTests.user)

    def test_urls_uses_correct_template(self):
        """Namespace:name использует соответствующий шаблон
        в приложении users."""
        templates_url_names = {
            UsersViewsTests.password_change_form:
            'users/password_change_form.html',
            UsersViewsTests.logout:
            'users/logged_out.html',
            UsersViewsTests.login:
            'users/login.html',
            UsersViewsTests.signup:
            'users/signup.html',
            UsersViewsTests.password_reset_done:
            'users/password_reset_done.html',
            UsersViewsTests.password_reset_form:
            'users/password_reset_form.html',
            # UsersViewsTests.password_reset_confirm:
            # 'users/password_reset_confirm.html',
            UsersViewsTests.password_reset_complete:
            'users/password_reset_complete.html',
        }
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)

    def test_post_create_edit_show_correct_context(self):
        """На страницу users:signup в контексте передаётся форма
        для создания нового пользователя."""
        name = UsersViewsTests.signup

        with self.subTest(name=name):
            response = self.guest_client.get(name)
            form_fields = {
                'first_name': forms.fields.CharField,
                'last_name': forms.fields.CharField,
                'username': forms.fields.CharField,
                'email': forms.fields.EmailField,
                'password1': forms.fields.CharField,
                'password2': forms.fields.CharField,
            }
            for value, expected in form_fields.items():
                with self.subTest(value=value):
                    form_field = response.context.get('form').fields.get(value)
                    self.assertIsInstance(form_field, expected)
