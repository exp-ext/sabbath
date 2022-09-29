from django.test import Client, TestCase
from django.urls import reverse


class AboutViewsTests(TestCase):
    author = reverse('about:author')
    tech = reverse('about:tech')

    def setUp(self):
        self.guest_client = Client()

    def test_pages_codes_by_namespace(self):
        """Страницы по namespace:name доступны любому пользователю
        в приложении about."""
        code_ok = 200
        url_names = [
            [self.guest_client, AboutViewsTests.author, code_ok],
            [self.guest_client, AboutViewsTests.tech, code_ok],
        ]
        for client, address, code in url_names:
            with self.subTest(address=address):
                response = client.get(address)
                self.assertEqual(code, response.status_code)

    def test_urls_about_correct_template(self):
        """Namespace:name использует соответствующий шаблон
        в приложении about."""
        templates_url_names = {
            AboutViewsTests.author: 'about/author.html',
            AboutViewsTests.tech: 'about/tech.html',
        }
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertTemplateUsed(response, template)
