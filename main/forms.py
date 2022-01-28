from .models import Usernames
from django.forms import ModelForm, TextInput


class UsernamesForm(ModelForm):
    class Meta:
        model = Usernames
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введіть ваше ім'я"
            })
        }
