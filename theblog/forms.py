from django import forms
from .models import *
from tinymce.widgets import TinyMCE

from django import forms
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'categories')
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            # 'categories': forms.CheckboxSelectMultiple(),
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
