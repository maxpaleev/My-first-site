from .models import Work
from django.forms import ModelForm, TextInput, Textarea


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ['day', 'rus', 'alg', 'lit', 'bio', 'his', 'geo', 'eng', 'science', 'inf', 'IZO', 'teh',
                  'deutsch', 'geometria', 'fiz', 'date']

        widgets = {
            'day': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'День недели'
            }),
            'rus': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Русский'
            }),
            'alg': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Алгебра'
            }),
            'fiz': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Физика'
            }),
            'geometria': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Геометрия'
            }),
            'lit': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Лит-ра'
            }),
            'bio': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Биология'
            }),
            'eng': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Английский'
            }),
            'IZO': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Изо'
            }),
            'inf': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информатика'
            }),
            'geo': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'География'
            }),
            'his': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'История'
            }),
            'science': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Общество'
            }),
            'teh': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Технология'
            }),
            'deutsch': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Немецкий'
            }),
            'date': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
        }
