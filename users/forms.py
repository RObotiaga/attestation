from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'city')


class CustomUserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('city', 'phone', 'avatar',)
