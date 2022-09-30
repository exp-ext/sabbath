from core.models import CreatedModel
from django.contrib.auth import get_user_model
from django.db import models
from pytils.translit import slugify
from sorl.thumbnail import ImageField

# from upload.models import Photo

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True)
    description = models.TextField()
    image = models.ImageField(
        verbose_name='Лого_группы',
        upload_to='group/',
        blank=True
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:100]
        super().save(*args, **kwargs)


class Post(CreatedModel):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст поста'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост'
    )
    image = ImageField(
        verbose_name='Картинка',
        upload_to='posts/',
        blank=True
    )
    # image = models.ForeignKey(
    #     Photo,
    #     on_delete=models.SET_NULL,
    #     related_name='photo',
    #     verbose_name='Фотография',
    #     help_text='Фотография к посту'
    # )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.text[:15]


class Comment(CreatedModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарии',
        help_text='Комментарии поста'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите текст комментария'
    )

    def __str__(self) -> str:
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = (models.UniqueConstraint(
            fields=('author', 'user'),
            name='unique_follower'),
        )

    def __str__(self):
        return f'{self.user} follows {self.author}'
