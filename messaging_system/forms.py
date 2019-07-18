from django.contrib.auth.models import User
from .models import Message
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(error_messages={'unique': 'This email is already exist'})
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('password', "password and confirm_password does not match")
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class MessageForm(forms.ModelForm):
    USER_EMAIL_CHOICES = ((u.email, u.email) for u in User.objects.all())

    receiver = forms.ChoiceField(choices=USER_EMAIL_CHOICES, widget=forms.Select)

    class Meta:
        model = Message
        fields = ('receiver', 'content', 'subject')
