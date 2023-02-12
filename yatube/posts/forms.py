from django import forms
from django.forms import Textarea

from .models import Comment, Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'group', 'image')

    def clean_text(self):
        data = self.cleaned_data['text']
        if Post.objects.filter(text=data).exists():
            raise forms.ValidationError(
                'Уже есть текст с таким постом...'
            )
        return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'rows': 2, 'cols': 10}),
        }
