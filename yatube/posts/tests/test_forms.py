import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from ..forms import PostForm
from ..models import Comment, Group, Post, User

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)
SMALL_GIF = (
    b'\x47\x49\x46\x38\x39\x61\x02\x00'
    b'\x01\x00\x80\x00\x00\x00\x00\x00'
    b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
    b'\x00\x00\x00\x2C\x00\x00\x00\x00'
    b'\x02\x00\x01\x00\x00\x02\x02\x0C'
    b'\x0A\x00\x3B'
)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PostFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_author = User.objects.create_user(
            username='auth',
            password='1234GLKLl5',
            phone_number='+799988776611'
        )
        cls.user_action = User.objects.create_user(
            username='comment_auth',
            password='123TKLDKlk45',
            phone_number='+799988776622'
        )
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание'
        )
        cls.post = Post.objects.create(
            author=cls.user_author,
            text='Тестовый пост'
        )
        cls.form = PostForm()
        cls.profile = reverse(
            'posts:profile',
            kwargs={'username': cls.post.author}
        )
        cls.post_edit = reverse(
            'posts:post_edit',
            kwargs={'post_id': cls.post.id}
        )
        cls.post_detail = reverse(
            'posts:post_detail',
            kwargs={'post_id': cls.post.id}
        )
        cls.post_create = reverse('posts:post_create')
        cls.add_comment = reverse(
            'posts:add_comment',
            kwargs={'post_id': cls.post.id}
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user_author)

        self.comment_authorized_client = Client()
        self.comment_authorized_client.force_login(self.user_action)

        self.uploaded_gif = SimpleUploadedFile(
            name='small.gif',
            content=SMALL_GIF,
            content_type='image/gif'
        )

    def test_post_create_forms(self):
        """Валидная форма создает запись в Posts."""
        posts_count = Post.objects.count()
        form_data = {
            'text': 'Тестовый пост 1',
            'group': self.group.id,
            'image': self.uploaded_gif
        }
        response = self.authorized_client.post(
            self.post_create,
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, self.profile)
        self.assertTrue(
            Post.objects.filter(
                text='Тестовый пост 1',).exists()
        )
        self.assertEqual(Post.objects.count(), posts_count + 1)

    def test_post_edit_form(self):
        """Валидная форма изменяет запись в Posts."""
        posts_count = Post.objects.count()
        self.assertTrue(
            Post.objects.filter(text='Тестовый пост').exists()
        )
        form_data = {
            'text': 'Тестовый пост after the change',
            'group': self.group.id,
            'image': self.uploaded_gif,
        }
        response = self.authorized_client.post(
            self.post_edit,
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, self.post_detail)

        self.assertEqual(
            Post.objects.get(text='Тестовый пост after the change',
                             group=self.group.id).text,
            'Тестовый пост after the change'
        )
        self.assertEqual(Post.objects.count(), posts_count)
        self.assertFalse(Post.objects.filter(text='Тестовый пост').exists())

    def test_comment(self):
        """Комментарий постов работает нормально только у авторизованного
        пользователя."""
        post = Post.objects.get(id=1)
        camments_from_post = post.comments.count()

        form_data = {
            'text': 'Новый комментарий',
        }
        response = self.comment_authorized_client.post(
            self.add_comment,
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, self.post_detail)
        comment = Comment.objects.first()
        self.assertEqual(comment.text, form_data['text'])
        self.assertEqual(post.comments.count(), camments_from_post + 1)
        response = self.authorized_client.get(self.post_detail)
        comments = response.context['comments'][0]
        self.assertEqual(comments.text, form_data['text'])
