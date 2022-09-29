from django.test import Client, TestCase


class ViewTestClass(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_error_page(self):
        """Проверка обработки ошибки 404."""
        code_not_found = 404

        response = self.guest_client.get('/nonexist-page/')

        self.assertEqual(
            response.status_code,
            code_not_found,
            f'статус ответа {response.status_code} не соответствует '
            'ожидаемому - 404'
        )
        self.assertTemplateUsed(
            response,
            'core/404.html',
            'шаблон для страницы 404 не соответствует ожидаемуму'
        )
