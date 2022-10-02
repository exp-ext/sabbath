from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phoneNumberRegex = RegexValidator(
        regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    )
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        unique=True,
        verbose_name='Номер телефона',
        help_text='Введите свой номер телефона'
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Немножко о себе',
        help_text='Личные интересы, цели, предпотения'
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Место проживания',
        help_text='Страна, Город'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
        help_text='Если хотите подарок на ДР'
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='avatar/',
        default='avatar/NLO.png',
        null=True,
        blank=True
    )
