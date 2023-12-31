from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'intro': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            }),
        }