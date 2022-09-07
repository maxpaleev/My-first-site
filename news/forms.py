from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назавание статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'date': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }
