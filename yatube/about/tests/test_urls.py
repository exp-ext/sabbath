from django.test import Client, TestCase


class AboutURLTests(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_pages_codes_by_url(self):
        """Страницы по URL доступны любому пользователю в приложении about."""
        code_ok = 200
        url_names = [
            [self.guest_client, '/about/author/', code_ok],
            [self.guest_client, '/about/tech/', code_ok],
        ]
        for client, address, code in url_names:
            with self.subTest(address=address):
                response = client.get(address)
                self.assertEqual(code, response.status_code)
