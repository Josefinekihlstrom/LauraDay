from django import forms
from .models import Post, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
