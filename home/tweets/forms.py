from django import forms
from .models import Tweet


class tweetForm(forms.ModelForm):
    class Meta :
        model = Tweet
        fields = ['text' , 'photo']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'What’s happening?'
            }),
        }
        