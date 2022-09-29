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
            'bio',
            'location',
            'birth_date',
            'avatar'
        )
