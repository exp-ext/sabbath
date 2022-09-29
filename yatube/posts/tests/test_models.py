from django.test import TestCase
from posts.models import Group, Post, User


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание'
        )

    def test_group_have_correct_object_names(self):
        """Проверяем, что у модели корректно работает __str__."""
        group = self.group
        str_text = group.title
        self.assertEqual(
            str_text,
            str(group),
            f'У модели Group результат __str__ = "{str_text}" '
            f'не соответствует ожидаемуму "{str(group)}"'
        )


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост. ' * 3
        )

    def test_posts_have_correct_object_names(self):
        """Проверяем, что у модели корректно работает __str__."""
        post = self.post
        str_text = post.text[:15]
        self.assertEqual(
            str_text,
            str(post),
            f'У модели Post результат __str__ = "{str_text}" '
            f'не соответствует ожидаемуму "{str(post)}"'
        )

    def test_field_description_name(self):
        """verbose_name и help_text совпадает с ожидаемым."""
        field_verboses = {
            'text': 'Текст поста',
            'pub_date': 'Дата создания',
            'author': 'Автор',
            'group': 'Группа',
        }
        field_help_text = {
            'text': 'Введите текст поста',
            'group': 'Группа, к которой будет относиться пост'
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                meta_field = self.post._meta.get_field(field)
                self.assertEqual(
                    meta_field.verbose_name,
                    expected_value,
                    f'verbose_name поля {field} не соответствует '
                    f'ожидаемуму "{expected_value}"'
                )
                if field in field_help_text:
                    self.assertEqual(
                        meta_field.help_text,
                        field_help_text[field],
                        f'help_text поля {field} не соответствует '
                        f'ожидаемуму "{field_help_text[field]}"'
                    )
