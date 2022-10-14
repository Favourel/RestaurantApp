from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     check_email = User.objects.filter(email=email).exists()
    #     if check_email:
    #         raise forms.ValidationError("Email already exists.")


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "address"]
