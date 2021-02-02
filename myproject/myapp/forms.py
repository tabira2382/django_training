from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Post_comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post_comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'textarea'})
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
