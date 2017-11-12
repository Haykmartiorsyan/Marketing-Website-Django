from django import forms
from .models import PostComment
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        fields = ('name', 'last_name', 'email', 'subject', 'message')
        model = PostComment
