from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BootstrapUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        labels = {
            "username": "Логін",
            # password1 та password2 не будуть взяті звідси
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # додаємо клас bootstrap
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
        # змінюємо лейбли для паролів тут
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Підтвердження пароля"
