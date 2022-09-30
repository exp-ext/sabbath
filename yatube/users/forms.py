from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class CreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
        )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'location',
            'birth_date',
            'bio',
        )
