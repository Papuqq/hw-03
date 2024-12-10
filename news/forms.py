from django import forms
from .models import Post
from allauth.account.forms import SignupForm
from django.core.mail import send_mail


class PostForms(forms.ModelForm):
    header = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'header',
            'text',
            'category',
            'author',
        ]


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        send_mail(
            subject='Добро пожаловать в наш интернет-магазин!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )
        return user
