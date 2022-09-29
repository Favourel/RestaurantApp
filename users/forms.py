from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.forms import forms


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        check_email = User.objects.filter(email=email).exists()
        if check_email:
            raise forms.ValidationError("Email already exists.")
        return check_email
