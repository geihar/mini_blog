from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

User = get_user_model()


class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdate(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileImg(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileImg, self).__init__(*args, **kwargs)
        self.fields["img"].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ["img"]
