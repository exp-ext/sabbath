from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Photo(models.Model):
    User = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.SET_NULL
    )
    file = models.ImageField(
        upload_to=user_directory_path
    )
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
