from .models import Work
from django.forms import ModelForm, TextInput, DateTimeInput


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ['day', 'rus', 'match', 'lit', 'date', 'bio', 'his', 'geo', 'eng', 'science', 'inf', 'IZO', 'teh',
                  'deutsch']

        widgets = {
            'day': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'День недели'
            }),
            'rus': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Русский'
            }),
            'match': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Мат-ка'
            }),
            'lit': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Лит-ра'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            'bio': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Биология'
            }),
            'eng': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Английский'
            }),
            'IZO': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Изо'
            }),
            'inf': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Информатика'
            }),
            'geo': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'География'
            }),
            'his': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'История'
            }),
            'science': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Общество'
            }),
            'teh': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Технология'
            }),
            'deutsch': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Немецкий'
            }),
        }
