from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class CreationForm(UserCreationForm):
    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
            attrs={
                'id': "online_phone",
                'placeholder': "+7(___)___-__-__",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': "email",
                'placeholder': "name@domen.info",
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
        )


class ProfileForm(CreationForm):
    password = None
    birth_date = forms.CharField(
        label='Дата рождения',
        widget=forms.TextInput(
            attrs={
                'placeholder': "ДД.ММ.ГГГГ",
            }
        )
    )

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

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
